from django.urls import path, include
from accounts import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]