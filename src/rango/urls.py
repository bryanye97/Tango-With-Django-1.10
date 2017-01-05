from django.conf.urls import url
from rango import views as rango_views

urlpatterns = [
    url(r'^$', rango_views.index, name='index'),
    url(r'^about/', rango_views.about, name='about'),
]
