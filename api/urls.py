from django.urls import path
from api import views

urlpatterns = [
    path('', views.create, name='home'),
    path('<int:pk>', views.person, name='person'),
]