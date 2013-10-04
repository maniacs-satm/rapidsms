#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.utils.safestring import mark_safe

import django_tables2 as tables

from rapidsms.backends.database.models import INCOMING, BackendMessage


class MessageTable(tables.Table):

    def render_identity(self, record):
        # Render the phone number with an  arrow pointing to it
        # or away from it, depending on whether the message was going
        # out or coming in.
        if record.direction == INCOMING:
            return mark_safe(record.identity + "&nbsp;"
                             "<span class='arrow-left'>&larr;</span>")
        else:
            return mark_safe(record.identity + "&nbsp;"
                             "<span class='arrow-right'>&rarr;</span>")

    class Meta:
        model = BackendMessage
        sequence = ('date', 'identity', 'text')
        exclude = ('id', 'direction', 'name', 'message_id', 'external_id')
        order_by = ('-date', )
        attrs = {'id': 'log', 'class': 'messages'}
