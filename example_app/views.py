from inertia import render, inertia
from .models import Albums
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from core.views import InertiaDetailView, InertiaListView, InertiaCreateView, InertiaUpdateView
from django.urls import reverse_lazy

# Create your views here.
class AlbumListView(InertiaListView):
    model = Albums
    prop_name = "albums"
    inertia_view = "Albums/List"

class AlbumDetailView(InertiaDetailView):
    model = Albums
    prop_name = "album"
    inertia_view = "Albums/Detail"

class AlbumCreateView(InertiaCreateView):
    model = Albums
    inertia_view = "Albums/Create"
    prop_name="album"
    fields = ["artist", "title"]

class AlbumUpdateView(InertiaUpdateView):
    model = Albums
    inertia_view = "Albums/Update"
    prop_name = "album"
    fields = ["artist", "title"]

class AlbumDeleteView(DeleteView):
    model = Albums
    success_url = reverse_lazy("album_list_view")
