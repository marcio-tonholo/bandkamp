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
        return musician.albums.all()

# class MusicianAlbumSongView(APIView):
#     def get(self, request, musician_id, album_id):
#         musician = get_object_by_id(Musician ,musician_id)
#         album = get_object_by_id(Album, album_id)
#         songs = Song.objects.filter(musician=musician, album=album)

#         serializer = SongSerializer(songs, many=True)

#         return Response(serializer.data)

#     def post(self, request, musician_id, album_id):
#         musician = get_object_by_id(Musician, musician_id)

#         album = Album.objects.filter(musician=musician, id=album_id).first()

#         if not album:
#             return Response({'detail': 'Album not Found'}, status.HTTP_404_NOT_FOUND)

#         serializer = SongSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(album=album)

#         return Response(serializer.data, status.HTTP_201_CREATED)



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
