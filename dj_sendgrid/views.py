# -*- coding: utf-8 -*-
from django.views.generic import View

from .signals import (inbound_parse_event,
                      standard_webhook_event)

from braces.views import JSONResponseMixin

import json
import logging
logger = logging.getLogger('django.request')


class InboundParseWebhookView(JSONResponseMixin, View):
    """
    Handle the Sendgrid callback
    """
    http_method_names = [u'post',]

    json_dumps_kwargs = {'indent': 3}

    def dispatch(self, request, *args, **kwargs):
        logger.info('Recieved inbound parse webhook')
        return super(InboundParseWebhookView, self).dispatch(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST
        #
        # Send the event
        #
        inbound_parse_event.send(sender=self, **data)

        return self.render_json_response({
            'detail': 'Inbound Sendgrid Webhook recieved',
        })


class StandardEventWebhookView(JSONResponseMixin, View):
    """
    Handle the Sendgrid callback
    """
    http_method_names = [u'post',]

    json_dumps_kwargs = {'indent': 3}

    def dispatch(self, request, *args, **kwargs):
        logger.info('Recieved standard sendgrid webhook')
        return super(StandardEventWebhookView, self).dispatch(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        #
        # Send the event
        #
        standard_webhook_event.send(sender=self, data=json.loads(request.body))

        return self.render_json_response({
            'detail': 'Standard Sendgrid Webhook recieved',
        })