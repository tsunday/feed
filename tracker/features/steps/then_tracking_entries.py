from behave import then

from tracker.app_services.feed_tracker import FeedTrackerService


@then('there is {number_of_entries} tracking entry started at {time} with {minutes} minutes length for {user}')
def step(context, number_of_entries, time, minutes, user):
    reports = FeedTrackerService.get_daily_report(user=user)
    assert len(reports) == number_of_entries
    for report in reports:
        assert report.duration == minutes
        assert report.started_time == time
