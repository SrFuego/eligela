from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.views.static import serve


from apps.principal import urls as principal_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(principal_urls,
                      namespace='principal',
                      app_name='principal'
                      )
        ),
]

if settings.DEBUG:
    urlpatterns += [url(r'^media/(?P<path>.*)$',
                        serve,
                        {'document_root': settings.MEDIA_ROOT, }
                        ),
                    ]
