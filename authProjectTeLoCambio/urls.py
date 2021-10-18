"""authProjectTeLoCambio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>', views.UserDetailView.as_view()),
    path('user/update/<int:user>/<int:pk>', views.UserUpdateView.as_view()),
    path('profile/', views.ProfileCreateView.as_view()),
    path('profile/<int:user>/<int:pk>', views.ProfileDetailView.as_view()),
    path('profile/update/<int:user>/<int:pk>', views.ProfileUpdateView.as_view()),
    path('product/', views.ProductCreateView.as_view()),
    path('product/<int:user>/<int:pk>', views.ProductDetailView.as_view()),
    path('product/remove/<int:user>/<int:pk>', views.ProductDeteleView.as_view()),
    path('product/list/<int:user>', views.ProductUserListView.as_view()),
    path('product/update/<int:user>/<int:pk>', views.ProductUpdateView.as_view()),
    path('product/liststate/<int:user>', views.ProductUserListStateView.as_view()),
    path('exchange/', views.ExchangeCreateView.as_view()),
    path('exchange/<int:user>/<int:pk>', views.ExchangeDetailView.as_view()),
    path('exchange/list/origin/<int:user>', views.ExchangeUserOriginListView.as_view()),
    path('exchange/list/destination/<int:user>', views.ExchangeUserDestinationListView.as_view()),
    path('favorite/', views.FavoritesCreateView.as_view()),
    path('favorite/<int:user>/<int:pk>', views.FavoriteDetailView.as_view()),
    path('favorite/list/<int:user>', views.FavoriteUserListView.as_view()),
    path('favorite/update/<int:user>/<int:pk>', views.FavoriteUpdateView.as_view()),
]

