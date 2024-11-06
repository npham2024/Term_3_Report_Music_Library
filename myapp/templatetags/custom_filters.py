# myapp/templatetags/custom_filters.py
from django import template
import datetime

register = template.Library()


@register.filter
def format_duration(time_value):
    # Check if the input is a datetime.time object
    if isinstance(time_value, datetime.time):
        total_seconds = time_value.hour * 3600 + time_value.minute * 60 + time_value.second
    else:

        total_seconds = int(time_value)

    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes}:{seconds:02}"
