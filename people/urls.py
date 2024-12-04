from django.urls import path
from . import views


app_name = 'people'

urlpatterns = [
    path('list/', views.person_list, name='list')
]