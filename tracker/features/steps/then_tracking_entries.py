from behave import then

from tracker.app_services.feed_tracker import FeedTrackerService


@then('there is {number_of_entries:d} tracking entry with {minutes:d} minutes length for {user}')
@then('there are {number_of_entries:d} tracking entries with {minutes:d} minutes length for {user}')
def step(context, number_of_entries, minutes, user):
    reports = FeedTrackerService.get_daily_report(user=user)
    assert len(reports) == number_of_entries
    for report in reports:
        print(report.duration.seconds)
        assert report.duration.seconds == minutes*60
