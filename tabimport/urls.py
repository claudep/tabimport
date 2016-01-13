from django.conf.urls import url

from .forms import FileuploadForm, MatchingForm
from .views import DataImportView


urlpatterns = [
    url(r'^$', DataImportView.as_view([FileuploadForm, MatchingForm]), name='tabimport'),
]
