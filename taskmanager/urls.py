"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from tasks import views as task_views  

# Custom Admin Text
admin.site.site_header = "TaskForge Admin Panel"
admin.site.site_title = "TaskForge Admin"
admin.site.index_title = "Welcome to the TaskForge"

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Authentication
    path('signup/', task_views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name="tasks/login.html"), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Profile
    path('profile/', task_views.profile, name='profile'),

    # Home Dashboard
    path('', task_views.home, name='home'),

    # Built-in Auth URLs (like password reset)
    path('accounts/', include('django.contrib.auth.urls')),

    # Task CRUD URLs
    path('tasks/', task_views.task_list, name='task_list'),
    path('tasks/create/', task_views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', task_views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', task_views.task_delete, name='task_delete'),path('tasks/<int:pk>/toggle/', task_views.toggle_status, name='task_toggle'),
     path('tasks/<int:pk>/toggle/', task_views.toggle_status, name='toggle_status'),

]
