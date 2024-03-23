from django.urls import path
from relay import views

app_name = 'relay'

urlpatterns = [
    path('', views.home_page, name='home_page'),
]
