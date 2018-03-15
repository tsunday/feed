from django.utils import timezone

from tracker.models.feed_event import FeedEvent


class FeedEventRepository:
    @classmethod
    def save(cls, feed_event):
        feed_event.save()


    @classmethod
    def get_first_event_to_stop_for_user(cls, user):
        return FeedEvent.objects.get(user=user, duration=None)

    @classmethod
    def get_all_events_started_today_for_user(cls, user):
        return FeedEvent.objects.filter(user=user)