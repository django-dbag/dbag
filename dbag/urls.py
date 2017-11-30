from django.conf.urls import url
import dbag.views

urlpatterns = [
    url(r'^$', dbag.views.index,
        name="dbag-index"),
    url(r'^metric/([\w-]+)/$', dbag.views.metric_detail,
        name="dbag-metric-detail"),
    url(r'^metric/([\w-]+).json$', dbag.views.metric_json,
        name="dbag-metric-json"),
]
