from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.event_create, name='event_create'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/participate/', views.event_participate, name='event_participate'),
    path('register/', views.user_register, name='user_register'),
]

