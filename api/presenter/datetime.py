import json
from json import dumps


def millis(o):
    """
    Default JSON serializer.
    """
    import calendar, datetime
    if isinstance(o, datetime.datetime):
        if o.utcoffset() is not None:
            o = o - o.utcoffset()
        return int(calendar.timegm(o.timetuple()) * 1000 + o.microsecond / 1000)
    raise TypeError('Not sure how to serialize %s' % (obj,))


def iso(o):
    from datetime import date, datetime
    if type(o) is datetime.date or type(o) is datetime.datetime:
        return o.isoformat()
    if type(o) is decimal.Decimal:
        return float(o)


def strftime(o):
    from datetime import datetime, date
    return str(o).split('.')[0] if isinstance(o, (datetime, date)) else None


def format(o):
    return json.dumps(o, default=strftime)
