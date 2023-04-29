from django.contrib import admin
from characters.models import CSVFile

class CSVFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'download_date', 'last_edited')


admin.site.register(CSVFile, CSVFileAdmin)