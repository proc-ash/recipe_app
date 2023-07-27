from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.welcome, name='welcome'),
    path('delete_dish/<id>/',views.delete_dish,name='delete_dish'),
    path('update_dish/<id>/',views.update_dish,name='update_dish'),
]
