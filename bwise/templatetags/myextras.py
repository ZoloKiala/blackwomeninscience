from datetime import datetime, timedelta
from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter
def age(value): 
    start_date = datetime.datetime.utcnow() - value
    difference_in_days = start_date.days
    return difference_in_days
    # try:
    #     difference = now - value
    # except:
    #     return value

    # if difference <= timedelta(minutes=1):
    #     return 'just now'
    # return '%(time)s ago' % {'time': timesince(value).split(', ')[0]}

# register.filter('age', age)