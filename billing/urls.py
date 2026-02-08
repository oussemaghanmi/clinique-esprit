from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('', views.facture_list, name='list'),
]
