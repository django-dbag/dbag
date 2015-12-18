try:
    from django.conf.urls import patterns, include
except ImportError:  # Django 1.4
    from django.conf.urls.defaults import patterns, include

import dbag
dbag.autodiscover()

urlpatterns = patterns(
    '',
    (r'^dbag/', include('dbag.urls')),
)
