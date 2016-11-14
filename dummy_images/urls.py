from django.conf.urls import url

from . import views


app_name = 'dummy_images'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<resolution>[0-9]+x[0-9]+)/$', views.ImageView.as_view(), name='images')
]