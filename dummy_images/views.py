from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
import random

from .models import DummyImage


class ImageView(ListView):
    model = DummyImage
    template_name = 'dummy_images/images.html'

    def get_context_data(self, **kwargs):
        """Split resolution string by 'x' character."""
        width = self.kwargs['resolution'].split('x')[0]
        height = self.kwargs['resolution'].split('x')[1]

        dummy_images = DummyImage.objects.all()
        dummy_images_counter = DummyImage.objects.all().count(),
        
        random_image = get_object_or_404(DummyImage, pk=dummy_images[random.randrange(0, dummy_images_counter)].id)
        context = {'width': width, 'height': height, 'img': random_image, 'test': 'test'}

        return context


def index(request):
    return HttpResponse("Hello")
