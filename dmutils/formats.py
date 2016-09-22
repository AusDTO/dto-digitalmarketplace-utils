# -*- coding: utf-8 -*-
from datetime import datetime
import pytz

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
DATE_FORMAT = "%Y-%m-%d"
DISPLAY_SHORT_DATE_FORMAT = '%-d %B'
DISPLAY_DATE_FORMAT = '%A %-d %B %Y'
DISPLAY_TIME_FORMAT = '%H:%M:%S'
DISPLAY_DATETIME_FORMAT = '%A %-d %B %Y at %H:%M'

LOTS = [
    {
        'lot': 'saas',
        'lot_case': 'SaaS',
        'label': u'Software as a Service',
    },
    {
        'lot': 'paas',
        'lot_case': 'PaaS',
        'label': u'Platform as a Service',
    },
    {
        'lot': 'iaas',
        'lot_case': 'IaaS',
        'label': u'Infrastructure as a Service',
    },
    {
        'lot': 'scs',
        'lot_case': 'SCS',
        'label': u'Specialist Cloud Services',
    },
]


class DateFormatter(object):

    def __init__(self, tz_name='UTC'):
        self.timezone = pytz.timezone(tz_name)

    def _format(self, value, fmt):
        if not isinstance(value, datetime):
            value = datetime.strptime(value, DATETIME_FORMAT)
        if value.tzinfo is None:
            value = pytz.utc.localize(value)
        return value.astimezone(self.timezone).strftime(fmt)

    def timeformat(self, value):
        return self._format(value, DISPLAY_TIME_FORMAT)

    def shortdateformat(self, value):
        return self._format(value, DISPLAY_SHORT_DATE_FORMAT)

    def dateformat(self, value):
        return self._format(value, DISPLAY_DATE_FORMAT)

    def datetimeformat(self, value):
        return self._format(value, DISPLAY_DATETIME_FORMAT)


def lot_to_lot_case(lot_to_check):
    lot_i_found = [lot for lot in LOTS if lot['lot'] == lot_to_check]
    if lot_i_found:
        return lot_i_found[0]['lot_case']
    return None


def get_label_for_lot_param(lot_to_check):
    lot_i_found = [lot for lot in LOTS if lot['lot'] == lot_to_check]
    if lot_i_found:
        return lot_i_found[0]['label']
    return None
