from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('graphical/', views.graphical_method, name='graphical_method'),
    path('graphical/result/', views.graphical_result, name='graphical_result'),
    path('knapsack/', views.knapsack_method, name='knapsack_method'),
   
    path('simplex/', views.simplex_method, name='simplex_method'),
    path('transportation/', views.transportation_method, name='transportation_method'),
    path('transportation/result/', views.transportation_result, name='transportation_result'),  # Added this line for transportation result page
    path('optimization/', views.optimization, name='optimization'),
]
