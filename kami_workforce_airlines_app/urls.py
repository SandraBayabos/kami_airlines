from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('api/airplanes/', views.AirplaneAPIView.as_view(), name='airplanes'),
    path('api/airplanes/<int:airplane_id>/',
         views.AirplaneAPIView.as_view(), name='manage_airplane'),
    # path('api/airplanes/<int:airplane_id>/',
    #      views.AirplaneAPIView.as_view(), name='update_airplane'),
    # path('api/airplanes/<int:airplane_id>/delete/',
    #      views.AirplaneAPIView.as_view(), name='delete_airplane'),
]
