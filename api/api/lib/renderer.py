import datetime


def object_id_adapter(obj, request):
    return str(obj)


def datetime_adapter(obj, request):
        if isinstance(obj, datetime.datetime) and not obj.tzinfo:
            # If a datetime object has no timezone (naive
            # representation) set the
            # TZ to UTC.
            return obj.isoformat()

def set_adapter(obj, request):
    return list(obj)
