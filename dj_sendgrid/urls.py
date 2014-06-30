# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from .views import InboundParseWebhookView, StandardEventWebhookView


urlpatterns = patterns('',
    url(r'^webhook/inbound/$', csrf_exempt(InboundParseWebhookView.as_view()), name='inbound_event_webhook_callback'),
    url(r'^webhook/standard/$', csrf_exempt(StandardEventWebhookView.as_view()), name='standard_event_webhook_callback'),
)
