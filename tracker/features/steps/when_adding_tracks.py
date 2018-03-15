from behave import when

from tracker.app_services.feed_tracker import FeedTrackerService


@when('user {user} starts event today at {time}')
def step(context, user, time):
    FeedTrackerService.start_event(user)


@when('user {user} stops event today at {time}')
def step(context, user, time):
    FeedTrackerService.stop_event(user)


@when('user {user} registers {minutes} minutes length event at {time}')
def step(context, user, minutes, time):
    FeedTrackerService.log_event(user=user, duration=minutes)
