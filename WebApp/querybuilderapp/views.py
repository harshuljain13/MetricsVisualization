from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from django.apps import apps
import json
import sqlite3
import re
import pandas as pd
from django.db import connection
import collections


myapp = apps.get_app_config('querybuilderapp')
models_dict = myapp.models


def get_model_fields(model):
    field_objs = model._meta.fields
    model_fields_map = collections.OrderedDict()
    for field_obj in field_objs:
        model_fields_map[field_obj.name]=field_obj.get_internal_type()
    return model_fields_map

# Create your views here.
def home(request):
    return render(request, 'querybuilderapp/index.html', context={'tables': models_dict})

def get_schema_details(request):
    model_str = request.POST.get('table_name', None)
    model_class = models_dict[model_str]
    model_fields_map = get_model_fields(model_class)
    return JsonResponse(model_fields_map, safe=False)

def get_query_data(request):
    sql_query = request.POST.get('sql_query', None)
    agg_type = request.POST.get('agg_type', None)
    model_str = request.POST.get('table_name', None)
    xaxis_column = request.POST.get('xaxiscolumn', None)
    yaxis_column = request.POST.get('yaxiscolumn', None)

    # get the table columns and their types
    model_class = models_dict[model_str]
    model_fields_map = get_model_fields(model_class)
    print(model_fields_map)

    data_df = pd.read_sql_query(sql_query, connection)

    valid_date_time_fields = ['DateField', 'TimeField', 'DateTimeField']

    if agg_type=='None':
        #check datetime column
        if model_fields_map[xaxis_column] in valid_date_time_fields:
            data_df[xaxis_column] = pd.to_datetime(data_df[xaxis_column])
        #convert dataframe to series
        data_df = data_df.set_index(xaxis_column)

    highcharts_json = series_to_highcharts(data_df, xaxis_column, yaxis_column)
    print(highcharts_json)

    return JsonResponse(highcharts_json, safe=False)


def series_to_highcharts(series, xaxiscol, yaxiscol):
    series_json = json.loads(series.to_json())[yaxiscol]
    data = [[float(key),float(value)] for key,value in series_json.items()]
    final_json = {}
    final_json['xlabel'] = xaxiscol
    final_json['ylabel'] = yaxiscol
    final_json['data'] = sorted(data, key=lambda x: x[0])

    return final_json
