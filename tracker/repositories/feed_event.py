from tracker.models.feed_event import FeedEvent


class FeedEventRepository:
    @classmethod
    def save(cls, feed_event):
        feed_event.save()


    @classmethod
    def get_first_event_to_stop_for_user(cls, user):
        return FeedEvent.objects.get(user=user, duration=None)