from datetime import datetime
from unittest.mock import patch

from behave import when
from django.utils import timezone

from tracker.app_services.feed_tracker import FeedTrackerService


def parse_time(time):
    time = datetime.strptime(time, '%H:%M').time()
    return datetime.combine(timezone.now(), time).replace(tzinfo=timezone.now().tzinfo)


@when('user {user} starts event today at {time}')
def step(context, user, time):
    with patch.object(timezone, 'now', return_value=parse_time(time)):
        FeedTrackerService.start_event(user)


@when('user {user} stops event today at {time}')
def step(context, user, time):
    with patch.object(timezone, 'now', return_value=parse_time(time)):
        FeedTrackerService.stop_event(user)


@when('user {user} registers {minutes:d} minutes length event at {time}')
def step(context, user, minutes, time):
    FeedTrackerService.log_event(user=user, duration_in_minutes=minutes)
