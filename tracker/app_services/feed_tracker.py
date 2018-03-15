from tracker.models.feed_event import FeedEvent
from tracker.repositories.feed_event import FeedEventRepository


class FeedTrackerService:
    @classmethod
    def start_event(cls, user):
        feed_event = FeedEvent(user=user)
        FeedEventRepository.save(feed_event=feed_event)

    @classmethod
    def stop_event(cls, user):
        feed_event = FeedEventRepository.get_first_event_to_stop_for_user(user)
        feed_event = feed_event.stop()
        FeedEventRepository.save(feed_event)

    @classmethod
    def log_event(cls, user, duration):
        feed_event = FeedEvent(user=user, duration=duration)
        FeedEventRepository.save(feed_event)

    @classmethod
    def get_daily_report(cls, user):
        return list(FeedEventRepository.get_all_events_started_today_for_user(user))
