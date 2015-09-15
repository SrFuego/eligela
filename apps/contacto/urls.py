# Python imports


# Django imports
from django.conf.urls import url


# Local imports
from .views import ContactanosView

# Create your tests here.


urlpatterns = [
    url(r'^$', ContactanosView.as_view(), name='index'),
]
