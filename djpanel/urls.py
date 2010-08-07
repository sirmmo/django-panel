from django.conf.urls.defaults import *



urlpatterns = patterns('',
  
    (r'^$', 'djpanel.views.list'),
    (r'^(?P<panel>.*)$', 'djpanel.views.panel'),
)