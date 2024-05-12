from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView

# Create your views here.

def list(request):
    notes = Notes.objects.all()
    return render(request,'notes/note_list.html',{'notes':notes})

def detail(request,pk):
    try:
        note = Notes.objects.get(pk=pk)
    except:
        raise Http404("note doesn't exist")
    return render(request,'notes/note_detail.html',{'note':note})
