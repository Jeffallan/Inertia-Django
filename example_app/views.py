from inertia import render, inertia
from .models import Albums
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from core.views import (InertiaDetailView, 
                        InertiaListView,  
                        InertiaUpdateOrCreateView)
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django import forms
from .models import Albums

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Albums
        exclude = ["id"]
        error_messages = {
            'title': {
                'unique': (f"An album with that title already exists"),
            },
        }

# Create your views here.
class AlbumListView(InertiaListView):
    model = Albums
    prop_name = "albums"
    inertia_view = "Albums/List"

class AlbumDetailView(InertiaDetailView):
    model = Albums
    prop_name = "album"
    inertia_view = "Albums/Detail"

class AlbumCreateView(InertiaUpdateOrCreateView):
    model = Albums
    inertia_view = "Albums/Create"
    prop_name="album"
    fields = ["artist", "title"]
    redirect_url = reverse_lazy("album_list_view")

class AlbumUpdateView(InertiaUpdateOrCreateView):
    model = Albums
    inertia_view = "Albums/Update"
    prop_name = "album"
    fields = ["artist", "title"]
    redirect_url = reverse_lazy("album_list_view")
    form_class = AlbumForm

class AlbumDeleteView(DeleteView):
    model = Albums
    success_url = reverse_lazy("album_list_view")
