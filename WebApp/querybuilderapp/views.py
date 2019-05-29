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


myapp = apps.get_app_config('querybuilderapp')
models_dict = myapp.models


def get_model_fields(model):
    field_objs = model._meta.fields
    fields = list(map(lambda x: (x.name, x.get_internal_type()), field_objs))
    return fields

# Create your views here.
def home(request):
    return render(request, 'querybuilderapp/index.html', context={'tables': models_dict})

def get_schema_details(request):
    model_str = request.POST.get('table_name', None)
    model_class = models_dict[model_str]
    model_attr = get_model_fields(model_class)
    return JsonResponse(model_attr, safe=False)

def get_query_data(request):
    sql_query = request.POST.get('sql_query', None)
    agg_type = request.POST.get('agg_type', None)
    model_str = request.POST.get('table_name', None)

    model_class = models_dict[model_str]
    model_attr = get_model_fields(model_class)
    print(model_attr)
    parse_dates = {}
    for column, column_type in model_attr:
        if column_type == 'DateTimeField':
            parse_dates[column] = {'format': '%d/%m/%y %H:%M'}

    print(parse_dates)

    df = pd.read_sql_query(sql_query, connection, parse_dates=['RecordDateTime'])

    print(df.dtypes)

    return JsonResponse(model_attr, safe=False)


