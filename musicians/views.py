from rest_framework import generics
from albums.models import Album
from albums.serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from songs.models import Song
from songs.serializers import SongSerializer

from .models import Musician
from .serializers import MusicianSerializer


class MusicianView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianAlbumView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer



    def perform_create(self,serializer):
        musician_id = self.request.path.split("/")[3]
        musician = get_object_or_404(Musician,id = musician_id )
        serializer.save(musician=musician)  

    def get_queryset(self):
        musician_id = self.request.path.split("/")[3]
        musician = get_object_or_404(Musician,id = musician_id )

        route_parameter_gt = self.request.GET.get("duration_gt")
        route_parameter_lt = self.request.GET.get("duration_lt")

        if route_parameter_gt:
            queryset = []
            for i in  range(len(musician.albums.all())):
                total_duration = AlbumSerializer(musician.albums.all()[i]).data["total_duration"]
                if total_duration > int(route_parameter_gt): 
                    queryset.append(musician.albums.all()[i])
            return queryset

        route_parameter_lt = self.request.GET.get("duration_lt")

        if route_parameter_lt:
            queryset = []
            for i in  range(len(musician.albums.all())):
                total_duration = AlbumSerializer(musician.albums.all()[i]).data["total_duration"]
                if total_duration < int(route_parameter_lt): 
                    queryset.append(musician.albums.all()[i])
            return queryset    

        
        return musician.albums.all()


class MusicianAlbumSongView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self,serializer):
        musician_id = self.request.path.split("/")[3]
        album_id = self.request.path.split("/")[5]
        album = get_object_or_404(Album,id = album_id)
        musician = get_object_or_404(Musician,id = musician_id )
        serializer.save(album=album)

    def get_queryset(self):
        album_id = self.request.path.split("/")[5]
        album = get_object_or_404(Album,id = album_id)
        return album.songs.all()        
