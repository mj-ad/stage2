from django.urls import path
from api import views

urlpatterns = [
    path('', views.post, name='home'),
    path('<int:pk>', views.get, name='get'),
    path('<int:pk>', views.update, name='update'),
    path('<int:pk>', views.delete, name='delete'),
]