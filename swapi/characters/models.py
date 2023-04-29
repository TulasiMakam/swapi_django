from django.db import models

class CSVFile(models.Model):
    file_name = models.CharField(max_length=100)
    download_date = models.DateTimeField('download_date')
    last_edited = models.DateTimeField('last_edited')

    class Meta:
        unique_together = ("id", "file_name", "download_date")

    def __str__(self):
        return self.file_name


