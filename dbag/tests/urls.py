from django.conf.urls import include, url

import dbag
dbag.autodiscover()

urlpatterns = [
    url(r'^dbag/', include('dbag.urls')),
]
