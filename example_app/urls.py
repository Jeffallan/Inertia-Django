from django.urls import path
from .views import AlbumListView, AlbumDetailView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView

#app_name="albums"

urlpatterns = [
    path("", AlbumListView.as_view(), name="album_list_view"),
    path("<int:pk>", AlbumDetailView.as_view(), name="album_detail_view"),
    path("add", AlbumCreateView.as_view(), name="album_create_view"),
    path("<int:pk>/edit", AlbumUpdateView.as_view(), name="album_edit_view"),
    path("<int:pk>/delete", AlbumDeleteView.as_view(), name="album_delete_view")
]

