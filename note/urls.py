# note\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.list_notes, name='list_notes'),
    path('create/', views.create_note, name='create_note'),
    path('update/<int:pk>/', views.update_note, name='update_note'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
    path('view/<int:pk>/', views.view_note, name='view_note'),
    path('notes/<int:note_pk>/posts/new/', views.create_post, name='create_post'),
    path('posts/<int:pk>/edit/', views.update_post, name='update_post'),
    path('posts/<int:pk>/delete/', views.delete_post, name='delete_post'),
]
