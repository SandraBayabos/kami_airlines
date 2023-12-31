from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('api/airplanes/', views.AirplaneAPIView.as_view(), name='airplanes'),
    path('api/airplanes/<int:airplane_id>/',
         views.AirplaneAPIView.as_view(), name='manage_airplane'),
]
