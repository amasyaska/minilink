from django.urls import path, re_path
from . import views

app_name = 'relay'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('create/', views.CreateLink.as_view(), name='create'),
    re_path(r'.+', views.RedirectTo.as_view(), name='redirect'),
]