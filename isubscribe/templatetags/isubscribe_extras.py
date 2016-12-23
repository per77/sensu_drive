from django import template
from django.conf import settings
import datetime
import os.path, time, json

DATETIME_FORMAT = settings.DATETIME_FORMAT
 
register = template.Library()


@register.filter
def epoch_datetime(epoch):
    
    DT = datetime.fromtimestamp(epoch).strftime(DATETIME_FORMAT)
    return "%s" % (DT)


@register.filter(name='entity_id')
def entity_id(value):
    return value.replace(":","_").replace(".","_")

@register.filter
def print_timestamp(timestamp):
    try:
        #assume, that timestamp is given in seconds with decimal point
        ts = float(timestamp)
    except ValueError:
        return None
    return datetime.datetime.fromtimestamp(ts).strftime(settings.EVENT_DATE_FORMAT)


@register.filter(name='status_int')
def status_int(value):
    return int(value)


@register.filter(name='js_bool')
def js_bool(value):
    if value == True:
        return json.dumps(value)
    if value == False:
        return json.dumps(value)
