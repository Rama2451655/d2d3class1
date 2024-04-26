from django.urls import path
from d2d3app.views import hello,d2d3
urlpatterns=[
    path('hello/',hello,name='hello'),
    path('',d2d3,name='d2d3'),
]