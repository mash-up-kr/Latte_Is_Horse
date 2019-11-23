from django.urls import path
from . import views

app_name = 'beverages'

urlpatterns = [
    path('', views.BeverageList.as_view(), name='BeverageList'),
]
