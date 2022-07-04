from django.urls import path

from . import views

urlpatterns = [
    path('musicians/', views.MusicianView.as_view()),
    path('musicians/<pk>/', views.MusicianDetailView.as_view()),
    path('musicians/<pk>/albums/', views.MusicianAlbumView.as_view()),
    path('musicians/<pk>/albums/<int:album_id>/songs/', views.MusicianAlbumSongView.as_view()),
]
