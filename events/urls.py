from django.urls import path
from events import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('create/event/', views.create_event, name='create_event'),
    path('edit/event/<str:pk>/', views.edit_event, name='edit_event'),
    path('delete/event/<str:pk>/', views.delete_event, name='delete_event'),
]