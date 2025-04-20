"""
URL configuration for djangoDiplomMagazin project.

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
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),

    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/profile/', views.index),
    path('accounts/login/', views.index),
    path('accounts/logout/', views.index),
    path('auth/registration/', views.registration, name='reg'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('forman/', views.forman, name='forman'),
    path('forwoman/', views.forwoman, name='forwoman'),
    path('forman/<str:cat2>', views.formancat, name='formancat'),
    path('forwoman/<str:cat2>', views.forwomancat, name='forwomancat'),
    path('otovare/<str:itemid>', views.otovare, name='otovare'),
    path('cart/edit/<int:itemid>/<str:num>', views.edit, name='edit'),
    path('cart/delete/<int:itemid>', views.delete, name='delete'),
    path('catalog/buy/<int:itemid>',views.buy, name='buy'),
    path('tolike/',views.tolike),
    path('forman/tolike/',views.tolike),
    path('forwoman/tolike/',views.tolike),

]
