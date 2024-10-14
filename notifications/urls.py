from django.urls import path
from . import views

urlpatterns = [
    path('receive-notification/', views.receive_notification, name='receive_notification'),
    path('list/', views.notifications_list, name='notifications_list'),
    path('drivers/', views.drivers_list, name='drivers_list'),
    path('combined/', views.combined_view, name='combined_view'),
]