from django.urls import path
from .views import CSVFileListView, fetch, starwars_view, value_count
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', CSVFileListView.as_view()),
    path('list/<int:id>', starwars_view, name='starwars_view'),
    path('fetch', fetch, name='fetch'), 
    path('value_count', value_count, name='value_count'),   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)