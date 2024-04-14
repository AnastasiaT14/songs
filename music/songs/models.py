from django.db import models

class SongWriter(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    picture = models.ImageField()
    bio = models.TextField(max_length=200)


class Song(models.Model):
    title = models.CharField(max_length=20)
    song_writer = models.ForeignKey(SongWriter, on_delete=models.CASCADE, related_name='songs')
    genre = models.CharField(max_length=100, default="genre")
    release_date = models.DateTimeField()