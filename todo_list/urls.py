"""todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers

from tasks.api import TaskViewSet, CountView

api_router = routers.DefaultRouter()
api_router.register('tasks', TaskViewSet, basename='tasks')

apiurls = ([
    path('', include(api_router.urls)),
    path('tasks/count', CountView.as_view(app='tasks', model='Task')),
    path('users/count', CountView.as_view(app='auth', model='User')),
], 'api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include(apiurls, namespace='api')),
]
