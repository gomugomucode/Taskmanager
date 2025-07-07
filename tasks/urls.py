from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),    
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('toggle-status/<int:pk>/', views.toggle_status, name='toggle_status'),
]
