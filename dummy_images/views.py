from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import random

from .models import DummyImage


def images(request, resolution):
    """Split resolution string by 'x' character."""
    width = resolution.split('x')[0]
    height = resolution.split('x')[1]

    dummy_images = DummyImage.objects.all()
    dummy_images_counter = DummyImage.objects.all().count()
    random_image = dummy_images[random.randrange(0, dummy_images_counter)]

    return render(request, 'dummy_images/images.html', {
        'width': width,
        'height': height,
        'img': random_image,
    })


def index(request):
    return HttpResponse("Hello")
