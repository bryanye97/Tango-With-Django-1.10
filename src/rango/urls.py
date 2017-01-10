from django.conf.urls import url
from rango import views as rango_views

app_name = 'rango'

urlpatterns = [
    url(r'^$', rango_views.index, name='index'),
    url(r'^about/$', rango_views.about, name='about'),
    url(r'^add_category/$', rango_views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', rango_views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', rango_views.add_page, name='add_page'),
    url(r'^register/', rango_views.register, name='register'),
    url(r'^login/', rango_views.user_login, name='login'),
    url(r'^logout/$', rango_views.user_logout, name='logout'),
    url(r'^restricted/', rango_views.restricted, name='restricted'),
]
