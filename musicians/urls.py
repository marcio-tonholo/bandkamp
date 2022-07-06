from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from . import views

urlpatterns = [
    path('musicians/', views.MusicianView.as_view()),
    path('musicians/<pk>/', views.MusicianDetailView.as_view()),
    path('musicians/<pk>/albums/', views.MusicianAlbumView.as_view()),
    path('musicians/<pk>/albums/<str:album_id>/songs/', views.MusicianAlbumSongView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


