from django.urls import  path
from app1.views import *
app_name='reddi'
TEMPLATE_DIR=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]