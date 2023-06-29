from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
 
    path('create_note', views.create_note_user),
    
    path('note_list',views.user_note_list), 
    path('delete/<int:note_id>',views.delete_note, name='delete_note'),
    #path('create_note_user/<str:username>/', views.create_note_user, name='create_note_user'),
    path('user_all',views.user_list),
    
   
    
    





] 
