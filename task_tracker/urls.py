from django.urls import path
from .views import home,home2,index,delete_task
urlpatterns = [

#     path('', home),
#     path('home2/', home2),
    path('', index ,name="index"),
     path('delete/<int:pk>',delete_task, name="delete"),
]
