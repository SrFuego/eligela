from django.conf.urls import url

from .views import IndexView, EntrevistaView, CarmenGitHubView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^entrevista/$', EntrevistaView.as_view(), name='entrevista'),
    url(r'^2016/$', CarmenGitHubView.as_view(), name='carmen'),
]
