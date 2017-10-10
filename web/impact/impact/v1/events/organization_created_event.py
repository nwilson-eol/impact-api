from datetime import datetime
from pytz import utc
from django.db.models import Q
from impact.utils import (
    DAWN_OF_TIME,
    next_instance,
    previous_instance,
)


class OrganizationCreatedEvent(object):
    EVENT_TYPE = "organization created"

    def __init__(self, organization):
        self.organization = organization

    @classmethod
    def events(cls, organization):
        return [cls(organization)]

    def serialize(self):
        earliest, latest = self._created_datetime()
        return {
            "datetime": earliest,
            "latest_datetime": latest,
            "event_type": self.EVENT_TYPE,
            "description": "",
            }

    def _created_datetime(self):
        startup = self.organization.startup_set.order_by("id").first()
        if startup:
            return _created_datetimes(startup)
        partner = self.organization.partner_set.order_by("id").first()
        if partner:
            return _created_datetimes(partner)
        return _created_datetimes(self.organization)


def _created_datetimes(instance):
    if instance.created_at is not None:
        return (instance.created_at, instance.created_at)
    if hasattr(instance, "created_datetime"):
        if instance.created_datetime is not None:
            return (instance.created_datetime,
                    instance.created_datetime)
        return (_previous_created_datetime(instance),
                _next_created_datetime(instance))
    query = Q(created_at__isnull=False)
    earliest = DAWN_OF_TIME
    previous = previous_instance(instance, query)
    if previous:
        earliest = previous.created_at
    latest = utc.localize(datetime.now())
    next = next_instance(instance, query)
    if next:
        latest = next.created_at
    return (earliest, latest)


def _previous_created_datetime(instance):
    prev = previous_instance(instance,
                             Q(created_datetime__isnull=False))
    if prev:
        return prev.created_datetime
    return DAWN_OF_TIME


def _next_created_datetime(instance):
    next = next_instance(instance,
                         Q(created_datetime__isnull=False))
    if next:
        return next.created_datetime
    return datetime.now()