from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Song(models.Model):
    # Song_ID = models.IntegerField(unique=True)
    Name_of_the_song = models.CharField(max_length=100)
    Duration_in_number_of_seconds = models.PositiveIntegerField()
    Uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name_of_the_song


class Podcast(models.Model):
    # Podcast_ID = models.IntegerField(unique=True)
    Name_of_the_podcast = models.CharField(max_length=100)
    PDuration_in_number_of_seconds = models.PositiveIntegerField()
    PUploaded_time = models.DateTimeField(auto_now_add=True)
    Host = models.CharField(max_length=100)
    Participants = ArrayField(models.CharField(max_length=100),
                              blank=True, size=10, default=list)

    def __str__(self):
        return self.Name_of_the_podcast


class Audiobook(models.Model):
    # Audiobook_ID = models.IntegerField(unique=True)
    Name_of_the_audiobook = models.CharField(max_length=100)
    Author_of_the_title = models.CharField(max_length=100)
    Narrator = models.CharField(max_length=100)
    ADuration_in_number_of_seconds = models.PositiveIntegerField()
    AUploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name_of_the_audiobook
