from django.urls import path
from . import views

app_name = 'relay'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('create/', views.CreateLink.as_view(), name='create'),
    path('<str:short_link>/', views.RedirectTo.as_view(), name='redirect'),
]