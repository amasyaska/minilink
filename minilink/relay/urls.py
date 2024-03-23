from django.urls import path
from . import CreateLink

app_name = 'relay'

urlpatterns = [
    path('create/', CreateLink.as_view(), name='create'),
]