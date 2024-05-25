from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.list ,name='note.list'),
    path('notes/<int:pk>',views.detail,name='notes.detail'),
    path('notes/new',views.NotesCreateView.as_view(),name='notes.add'),
    path('notes/<int:pk>/edit',views.NotesUpdateView.as_view(),name='notes.update'),

]
