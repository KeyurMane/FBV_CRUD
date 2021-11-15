from .views import *
from django.urls import path

urlpatterns = [
    path('v1/',dispview,name='disp'),
    path('v2/',createview,name='add'),
    path('updt/<int:id>/',updtview,name='updt'),
    path('delete/<int:id>/',delview,name='dlt')
]