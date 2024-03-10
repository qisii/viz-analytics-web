from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('viz1/', views.project1, name="viz-dengue-line"),
    path('viz2/', views.project2, name="viz-dengue-geo"),
    path('analytics1/', views.project3, name="analytics-mobilt"),
]