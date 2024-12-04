from django.urls import path
from . import views


app_name = 'people'

urlpatterns = [
    path('list/', views.person_list, name='list'),
    path('create/', views.person_create, name='create'),
    path('detail/<int:pk>/', views.person_detail ,name='detail'),
    path('delete/<int:pk>', views.person_delete, name='delete'),
]