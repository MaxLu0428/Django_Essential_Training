from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import CreateView,UpdateView,ListView,DetailView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
# Create your views here.

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/note_delete.html'

class NotesListView(ListView):
    model = Notes
    context_object_name='notes'
    template_name = 'notes/note_list.html'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name='note'
    template_name='notes/note_detail.html'

class NotesCreateView(CreateView):
    model = Notes
    form_class =NotesForm
    success_url='/smart/notes'

class NotesUpdateView(UpdateView):
    model = Notes
    form_class =NotesForm
    success_url='/smart/notes'