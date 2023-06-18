"""volProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import include, path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('api/total_items', views.total_items_sold, name='total_items_sold'),
    path('api/nth_most_total_item/', views.nth_most_total_item_view , name='nth_most_total_item_view'),
    path('api/percentage_of_department_wise_sold_items/', views.percentage_of_department_wise_sold_items,name='percentage_of_department_wise_sold_items' ),
    path('api/monthly_sales', views.monthly_sales , name = 'monthly_sales'),
]
