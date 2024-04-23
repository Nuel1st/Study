from django import template

register = template.Library()

@register.filter
def is_recent(timestamp):
    import datetime
    now = datetime.datetime.now(datetime.timezone.utc)
    return (now - timestamp).total_seconds() < 24 * 60 * 60


