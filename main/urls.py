"""booktime URL Configuration

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
from django.views.generic import TemplateView, DetailView
from main import views, forms
from . import models


urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("about-us/", TemplateView.as_view(template_name="about_us.html"), name="about_us"),
    path("contact-us/", views.ContactUsView.as_view(), name="contact_us"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("products/<slug:tag>/", views.ProductListView.as_view(), name="product_list"),
    path("product/<slug:slug>/", views.ProductDetailView.as_view(), name='product_detail'),
    path("address/", views.AddressListView.as_view(), name="address_list"),
    path("address/create/", views.AddressCreateView.as_view(), name="address_create"),
    path("address/<int:pk>", views.AddressUpdateView.as_view(), name="address_update"),
    path("address/<int:pk>/delete", views.AddressDeleteView.as_view(), name="address_delete"),
    path("add_to_basket/", views.add_to_basket, name="add_to_basket"),
    path("basket/", views.manage_basket, name="basket"),
    path("order/done", TemplateView.as_view(template_name="order_done.html"), name="checkout_done"),
    path("order/address_select/", views.AddressSelectionView.as_view(), name="address_select",)
]
