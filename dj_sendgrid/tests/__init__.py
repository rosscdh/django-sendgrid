# -*- coding: utf-8 -*-
INBOUND_POST_REQUEST = {
    'text': '',
    'html': '',
    'from': '',
    'to': '',
    'cc': '',
    'subject': '',
    'dkim': '',
    'SPF': '',
    'envelopeemail': '',
    'charsets': '',
    'spam_score': '',
    'spam_report': '',
    'attachments': '',
    'attachment-info': '',
    'attachmentX': ''
}

STANDARD_WEBHOOK_EVENT = [
  {
    "email": "john.doe@sendgrid.com",
    "timestamp": 1337197600,
    "smtp-id": "<4FB4041F.6080505@sendgrid.com>",
    "event": "processed"
  },
  {
    "email": "john.doe@sendgrid.com",
    "timestamp": 1337966815,
    "category": "newuser",
    "event": "click",
    "url": "http://sendgrid.com"
  },
  {
    "email": "john.doe@sendgrid.com",
    "timestamp": 1337969592,
    "smtp-id": "<20120525181309.C1A9B40405B3@Example-Mac.local>",
    "event": "processed"
  }
]

from .test_views import *