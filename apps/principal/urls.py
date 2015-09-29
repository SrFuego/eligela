from django.conf.urls import url

from .views import IndexView, EntrevistaView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^entrevista/$', EntrevistaView.as_view(), name='entrevista'),
]
