from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^conferencia/$', views.ConferenciaView.as_view(), name='conferencia'),
]
