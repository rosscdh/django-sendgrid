# -*- coding: utf-8 -*-
"""
Webhook signals
"""
from django.dispatch import Signal

#
# Outgoing Events
#
inbound_parse_event = Signal(providing_args=['text', 'html', 'from', 'to', 'cc', 'subject', 'dkim', 'SPF', 'envelopeemail', 'charsets', 'spam_score', 'spam_report', 'attachments', 'attachment-info', 'attachmentX',])  # event for handling incoming email events
standard_webhook_event = Signal(providing_args=['data'])  # standard webhook, bounce, unsubscribe, delivered, read etc..
