import django_tables2 as tables
from .models import CSVFile


class CSVListTable(tables.Table):
    file_name = tables.TemplateColumn('<a href="/list/{{record.id}}">{{record.file_name}}</a>')

    class Meta:
        model = CSVFile
        template_name = "django_tables2/bootstrap.html"
        fields = ("file_name",)


class CSVTable(tables.Table):
    name = tables.Column()
    height = tables.Column()
    mass = tables.Column()
    hair_color = tables.Column()
    skin_color = tables.Column()
    eye_color = tables.Column()
    birth_year = tables.Column()
    gender = tables.Column()
    homeworld = tables.Column()

    class Meta:
        attrs = {
            "id": "data_table"
            }
        

class DynamicTables(tables.Table):

    def __init__(self, *args, column_specs=(), **kwargs):
        bc = type(self.base_columns)(self.base_columns) # clone                                                                                                          
        for name, column in column_specs:
            self.base_columns[name] = column
        tables.Table.__init__(self, *args, **kwargs) # refers to static spec                                                                                          
        type(self).base_columns = bc # restore static spec

    class Meta:
        attrs = {
            "id": "dynamic_table"
        }