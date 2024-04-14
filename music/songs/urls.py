from django.urls import path
from .views import SongListView, SongDetailView, SongCreateView, SongUpdateView, SongDeleteView
from .views import SongWriterListView, SongWriterDetailView, SongWriterCreateView, SongWriterUpdateView, SongWriterDeleteView

urlpatterns = [
    path('songs/', SongListView.as_view(), name='song_list'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song_detail'),
    path('songs/create/', SongCreateView.as_view(), name='song_create'),
    path('songs/<int:pk>/update/', SongUpdateView.as_view(), name='song_update'),
    path('songs/<int:pk>/delete/', SongDeleteView.as_view(), name='song_delete'),
    path('songwriters/', SongWriterListView.as_view(), name='songwriter_list'),
    path('songwriters/<int:pk>/', SongWriterDetailView.as_view(), name='songwriter_detail'),
    path('songwriters/create/', SongWriterCreateView.as_view(), name='songwriter_create'),
    path('songwriters/<int:pk>/update/', SongWriterUpdateView.as_view(), name='songwriter_update'),
    path('songwriters/<int:pk>/delete/', SongWriterDeleteView.as_view(), name='songwriter_delete'),
]
