from behave import then

from tracker.app_services.feed_tracker import FeedTrackerService


@then('there is {number_of_entries:d} tracking entry with {minutes:d} minutes length for {user}')
@then('there are {number_of_entries:d} tracking entries with {minutes:d} minutes length for {user}')
def step(context, number_of_entries, minutes, user):
    reports = FeedTrackerService.get_daily_report(user=user)
    assert len(reports) == number_of_entries
    for report in reports:
        assert report.duration.seconds == minutes * 60


@then('daily report for {user} is not empty')
def step(context, user):
    assert not FeedTrackerService.is_daily_report_empty(user=user)


@then('daily report for {user} is empty')
def step(context, user):
    assert FeedTrackerService.is_daily_report_empty(user=user)


@then('last registered event for {user} took {minutes:d} minutes')
def step(context, user, minutes):
    assert FeedTrackerService.get_last_event(user).duration.seconds == minutes * 60