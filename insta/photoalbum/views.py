from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from photoalbum.forms import UploadFileForm
from photoalbum.models import Photo


class MainView(ListView):
    template_name = 'photoalbum/all_photos.html'
    context_object_name = 'all_photos'

    def get_queryset(self):
        return Photo.objects.all()

class AddPhotoView(CreateView):
    model = Photo
    fields = '__all__'
    success_url = reverse_lazy('main')

# class AddPhotoView(View):
#     def get(self, request):
#         form = UploadFileForm()
#         return render(request, 'photoalbum/photo_form.html',{"form":form})
#
#     def post(self, request):
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()

