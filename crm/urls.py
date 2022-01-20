from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('', views.crm_main, name='crm_main')
]