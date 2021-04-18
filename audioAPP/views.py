from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song, Podcast, Audiobook
from .serializers import SongSerializer, PodcastSerializer, AudiobookSerializer


# Create your views here.
@api_view(["POST", "GET"])
def create_list_audio(request, audioFileType):
    # Create given audiofiletype
    if request.method == "POST":
        if audioFileType.lower() == "song":
            serializer = SongSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response("Fill the data correctly")

        if audioFileType.lower() == "podcast":
            serializer = PodcastSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response("Fill the data correctly")

        if audioFileType.lower() == "audiobook":
            serializer = AudiobookSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response("Fill the data correctly")

        else:
            return Response("AudioType Not Exist")
    # retrive all the list of given audiotype
    if request.method == "GET":
        if audioFileType.lower() == "song":
            songs = Song.objects.all()
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif audioFileType.lower() == "podcast":
            podcasts = Podcast.objects.all()
            serializer = PodcastSerializer(podcasts, many=True)
            return Response(serializer.data)

        elif audioFileType.lower() == "audiobook":
            audiobooks = Audiobook.objects.all()
            serializer = AudiobookSerializer(audiobooks, many=True)
            return Response(serializer.data)

        else:
            return Response("AudioType Not Exist")

# retrieve and update perticular audiofiletype of given id
@api_view(["GET", "PUT"])
def get_update_audio(request, audioFileType, pk):
    if request.method == "GET":
        if audioFileType.lower() == "song":
            song = Song.objects.get(id=pk)
            serializer = SongSerializer(song, many=False)
            return Response(serializer.data)

        elif audioFileType.lower() == "podcast":
            podcast = Podcast.objects.get(id=pk)
            serializer = PodcastSerializer(podcast, many=False)
            return Response(serializer.data)

        elif audioFileType.lower() == "audiobook":
            audiobook = Audiobook.objects.get(id=pk)
            serializer = AudiobookSerializer(audiobook, many=False)
            return Response(serializer.data)
        else:

            return Response("AUDIO TYPE DOES NOT EXIST")

    if request.method == "PUT":
        if audioFileType.lower() == "song":
            song = Song.objects.get(id=pk)
            serializer = SongSerializer(instance=song, data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data)

        elif audioFileType.lower() == "podcast":
            podcast = Podcast.objects.get(id=pk)
            serializer = PodcastSerializer(instance=podcast, data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data)

        elif audioFileType.lower() == "audiobook":
            audiobook = Audiobook.objects.get(id=pk)
            serializer = AudiobookSerializer(instance=audiobook,
                                             data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data)

        else:
            return Response("AudioType Not Exist")

# delete the perticular audiofiletype of given id
@api_view(["DELETE"])
def delete_audio(request, audioFileType, pk):

    if audioFileType.lower() == "song":
        song = Song.objects.get(id=pk)
        song.delete()

        return Response("Song deleted")

    elif audioFileType.lower() == "podcast":
        podcast = Podcast.objects.get(id=pk)
        podcast.delete()

        return Response("Podcast Delete")

    elif audioFileType.lower() == "audiobook":
        audiobook = Audiobook.objects.get(id=pk)
        audiobook.delete()

        return Response("AudioBook deleted")

    else:
        return Response("AudioType Not Exist")
