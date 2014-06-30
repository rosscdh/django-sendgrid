django-sendgrid
====================

A Django app for integrating with sendgrid webhooks


Installation
------------

1. python setup.py
2. pip install requirements.txt
3. add dj_sendgrid to INSTALLED_APPS
4. add url to sendgrid endpoints
5. register url with sendgrid as webhook callback


__Example Implementation__

1. Setup your urls.py to use the view below as the callback reciever or just use the default sss reciever
2. Register the url "https://yourhost.com/sss/webhook/" as the webhook callback at sendgrid
3. and that is it, you can now hook up the signal listener and get a signal event whenever a webhook event happens

```
url(r'^sendgrid/', include('dj_sendgrid.urls', namespace='dj_sendgrid')),
```


__Please Note__

If you use the SnowshoeStampView then a signal will be issued when recieving callbacks from sendgrid, which you can then listen for and do other amazing things.


__Signal Example Implementation__


```signals.py
from django.dispatch import receiver

from sendgrid.signals import (inbound_parse_event,
                              standard_webhook_event)


@receiver(inbound_parse_event)
def on_sendgrid_inbound_parse_event(sender, text, html, from, to, cc, subject, dkim, SPF, envelopeemail, charsets, spam_score, spam_report, attachments, attachment-info, attachmentX, **kwargs):
    # do something amazing with the data passed in
    pass


@receiver(standard_webhook_event)
def standard_webhook_event(sender, data, **kwargs):
    # do something amazing with the data in the data object is usually a list
    pass
```
