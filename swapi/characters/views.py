
import csv
import json
import pandas as pd 
import django_tables2 as tables
from django.shortcuts import render
from .models import CSVFile
from django_tables2 import SingleTableView
from .tasks import fetch_and_download_data_from_api
from .tables import CSVListTable, CSVTable, DynamicTables
from django.conf import settings
from django.http import HttpResponseRedirect

class CSVFileListView(SingleTableView):
    model = CSVFile
    table_class = CSVListTable
    template_name = "home.html"

def fetch(request):
    fetch_and_download_data_from_api()
    
    return HttpResponseRedirect('/')

def starwars_view(request, id):
    csv_file = CSVFile.objects.get(pk=id)
    file_path = f"{settings.CSV_ROOT_PATH}/{csv_file.file_name}"
    input_file = csv.DictReader(open(file_path))
    table = CSVTable(input_file)

    return render(request, "detail_view.html", {
        "table": table,
        "file_name" : csv_file.file_name
    })

def value_count(request):
    
    file_name = (request.POST['file_name'])
    columns = request.POST.getlist('value_count')
    csv_file = CSVFile.objects.get(file_name=file_name)
    file_path = f"{settings.CSV_ROOT_PATH}/{csv_file.file_name}"
    df = pd.read_csv(file_path) 
    final_df = df.groupby(columns).size().reset_index(name='Count')
    json_records = final_df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    column_specs = []
    final_columns = final_df.head() 
    for i in final_columns:
        column_specs.append((i, tables.Column()))
    column_specs = tuple(column_specs)
    table = DynamicTables(column_specs=column_specs, data=data)

    return render(request, "occurrence.html", {
        "table": table,
        "file_name" : file_name
    })
