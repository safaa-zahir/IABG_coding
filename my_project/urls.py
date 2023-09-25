"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import re_path, include

#say hello back with the name of the person 
@api_view(['GET'])
def hello_world(request):
    return Response('Hello Mohamed Njeh!')


#returns the status of coding task
@api_view(['GET'])
def check_status(request):
    return Response({'Coding task': 'Successful'})

urlpatterns = [
    re_path(r'helloworld', hello_world),
    re_path(r'status', check_status)
]