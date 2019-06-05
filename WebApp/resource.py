import flask
import os
import logging
import requests
import json
import sys, inspect
import pandas as pd
from flask import Flask, url_for, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://:@'
db = SQLAlchemy(app)
conn = db.engine.connect().connection

from models import *

# Create your views here.
@app.route("/")
def home():
    model_module = sys.modules['models']
    models_dict = dict(inspect.getmembers(model_module, inspect.isclass))
    print(models_dict)
    return render_template('index.html', tables=models_dict)

@app.route("/getschemadetails", methods=['POST'])
def get_schema_details():
    model_module = sys.modules['models']
    models_dict = dict(inspect.getmembers(model_module, inspect.isclass))
    
    print(request.form)
    model_str = request.form.get('table_name', None)
    print 'model: ',model_str
    model_class = models_dict[model_str]
    
    model_fields_map = model_class.__columnsmap__
    print(model_fields_map)
    
    return jsonify(model_fields_map)

@app.route("/getquerydata", methods=['POST'])
def get_query_data():
    sql_query = request.form.get('sql_query', None)
    agg_type = request.form.get('agg_type', None)
    model_str = request.form.get('table_name', None)
    xaxis_column = request.form.get('xaxiscolumn', None)
    yaxis_column = request.form.get('yaxiscolumn', None)
    zaxis_column = request.form.get('zaxiscolumn', None)
    graph_type = request.form.get('graph_type',None)
    
    
    # get the table columns and their types
    model_module = sys.modules['models']
    models_dict = dict(inspect.getmembers(model_module, inspect.isclass))
    model_class = models_dict[model_str]
    model_fields_map = model_class.__columnsmap__
    print(model_fields_map)
    
    
    data_df = pd.read_sql_query(sql_query, conn)
    
    print(data_df)
    
    data_df.columns = map(lambda x: x.lower(), data_df.columns)
    
    valid_date_time_fields = ['datetime', 'date', 'time']
    #check datetime column
    if model_fields_map[xaxis_column] in valid_date_time_fields:
        data_df[xaxis_column] = pd.to_datetime(data_df[xaxis_column])
    if model_fields_map[yaxis_column] in valid_date_time_fields:
        data_df[yaxis_column] = pd.to_datetime(data_df[yaxis_column])
    
    final_json = {}
    final_json['xlabel'] = xaxis_column
    final_json['ylabel'] = yaxis_column
    if 'stack' in graph_type.lower():
        final_json['stacking'] = 'normal'
        final_json['graph_type'] = graph_type.lower().split(' ')[1]
    else:
        final_json['graph_type'] = graph_type.lower()
        final_json['stacking'] = ''
        
    if agg_type=='None':
        #convert dataframe to series
        data_df = data_df.set_index(xaxis_column)
        series_json = json.loads(data_df.to_json())[yaxis_column]
        if model_fields_map[xaxis_column] in valid_date_time_fields:
            data = [[float(key),float(value)] for key,value in series_json.items()]
        else:
            data = [[key,float(value)] for key,value in series_json.items()]
        data = sorted(data, key=lambda x: x[0])
        categories = map(lambda x: x[0], data)
        final_json['categories'] = categories
        final_json['xaxistype'] = model_fields_map[xaxis_column]
        series = []
        series.append({'name': 'Test', 'data': data})
        final_json['series'] = series
    else:
        if zaxis_column=='None':
            #move xaxis to index
            data_df = data_df.set_index(xaxis_column)
            series_json = json.loads(data_df.to_json())[yaxis_column]
            if model_fields_map[xaxis_column] in valid_date_time_fields:
                data = [[float(key),float(value)] for key,value in series_json.items()]
            else:
                data = [[key,float(value)] for key,value in series_json.items()]
            data = sorted(data, key=lambda x: x[0])
            categories = map(lambda x: x[0], data)
            final_json['categories'] = categories
            final_json['xaxistype'] = model_fields_map[xaxis_column]
            series = []
            series.append({'name': 'Test', 'data': data})
            final_json['series'] = series
        else:
            if model_fields_map[zaxis_column] in valid_date_time_fields:
                data_df[zaxis_column] = pd.to_datetime(data_df[zaxis_column])
            
            unique_xaxis_vals = data_df[xaxis_column].unique()
            unique_zaxis_vals = data_df[zaxis_column].unique()
            
            series = []
            categories = []
            for xaxis_val in unique_xaxis_vals:
                categories.append(xaxis_val)
                
            for zaxis_val in unique_zaxis_vals:
                filtered_df = data_df[data_df[zaxis_column]==zaxis_val]
                filtered_df = filtered_df.drop([zaxis_column], axis=1)
                filtered_df = filtered_df.set_index(xaxis_column)
                series_json = json.loads(filtered_df.to_json())[yaxis_column]
                data = [[key,float(value)] for key,value in series_json.items()]
                series.append({'name': zaxis_val, 'data':data})
                
            final_json['categories'] = categories
            final_json['series'] = series
            final_json['xaxistype'] = model_fields_map[xaxis_column]
    return jsonify(final_json)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=3200, debug=True)
