from django.urls import path, include
from check_in import views

urlpatterns = [
    path('', views.check_in, name='check_in'),
]
