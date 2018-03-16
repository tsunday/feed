from tracker.models.feed_event import FeedEvent


def before_scenario(context, scenario):
    FeedEvent.objects.all().delete()
