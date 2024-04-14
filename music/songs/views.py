from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import SongWriter, Song
from .forms import SongWriterForm, SongForm

class SongWriterListView(ListView):
    model = SongWriter
    template_name = 'songs/songwriter_list.html'
    context_object_name = 'songwriters'

class SongWriterDetailView(DetailView):
    model = SongWriter
    template_name = 'songs/songwriter_detail.html'

class SongWriterCreateView(CreateView):
    model = SongWriter
    form_class = SongWriterForm
    template_name = 'songs/songwriter_form.html'
    success_url = reverse_lazy('songwriter_list')

class SongWriterUpdateView(UpdateView):
    model = SongWriter
    form_class = SongWriterForm
    template_name = 'songs/songwriter_form.html'
    success_url = reverse_lazy('songwriter_list')

class SongWriterDeleteView(DeleteView):
    model = SongWriter
    template_name = 'songs/songwriter_confirm_delete.html'
    success_url = reverse_lazy('songwriter_list')

class SongListView(ListView):
    model = Song
    template_name = 'songs/song_list.html'
    context_object_name = 'songs'

class SongDetailView(DetailView):
    model = Song
    template_name = 'songs/song_detail.html'

class SongCreateView(CreateView):
    model = Song
    form_class = SongForm
    template_name = 'songs/song_form.html'
    success_url = reverse_lazy('song_list')

class SongUpdateView(UpdateView):
    model = Song
    form_class = SongForm
    template_name = 'songs/song_form.html'
    success_url = reverse_lazy('song_list')

class SongDeleteView(DeleteView):
    model = Song
    template_name = 'songs/song_confirm_delete.html'
    success_url = reverse_lazy('song_list')
