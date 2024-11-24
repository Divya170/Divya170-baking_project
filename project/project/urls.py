"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('product-gallery/', views.product_gallery, name='product_gallery'),
    path('order/', views.order_view, name='order'),
    path('about/', views.about_view, name='about'),  # About page URL pattern
    path('contact/', views.contact_view, name='contact'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
    path('index/', views.index, name='index'),  # Feedback form
]


    

