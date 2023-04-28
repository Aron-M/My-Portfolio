"""
URL configuration for pp4_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from my_pf.views import get_my_portfolio, personal_details, add_personal_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_my_portfolio, name='my_portfolio'),
    path('personal_details/', personal_details, name='personal_details'),
    path('personal_details/', add_personal_details, name='add_personal_details')
]
