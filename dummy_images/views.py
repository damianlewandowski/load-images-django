from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def images(request, resolution):
    """Split resolution string by 'x' character."""
    width = resolution.split('x')[0]
    height = resolution.split('x')[1]

    return render(request, 'dummy_images/images.html', {
        'width': width,
        'height': height,
    })


def index(request):
    return HttpResponse("Hello")
