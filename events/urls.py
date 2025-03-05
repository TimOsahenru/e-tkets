from django.urls import path
from events import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('create/event/', views.create_event, name='create_event'),
]