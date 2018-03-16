import datetime

from django.utils import timezone

from tracker.models.feed_event import FeedEvent
from tracker.repositories.feed_event import FeedEventRepository


class FeedTrackerService:
    @classmethod
    def start_event(cls, user):
        print('start called')
        feed_event = FeedEvent(user=user, started_at=timezone.now())
        FeedEventRepository.save(feed_event=feed_event)

    @classmethod
    def stop_event(cls, user):
        feed_event = FeedEventRepository.get_first_event_to_stop_for_user(user)
        feed_event = feed_event.stop()
        FeedEventRepository.save(feed_event)

    @classmethod
    def log_event(cls, user, duration_in_minutes):
        duration = datetime.timedelta(minutes=duration_in_minutes)
        feed_event = FeedEvent(user=user, duration=duration)
        FeedEventRepository.save(feed_event)

    @classmethod
    def get_daily_report(cls, user):
        return list(FeedEventRepository.get_all_events_started_today_for_user(user))

    @classmethod
    def get_last_event(cls, user):
        report = cls.get_daily_report(user)
        try:
            return report[-1]
        except IndexError as e:
            print(f'No reports exception: {e}')
            return None

    @classmethod
    def is_daily_report_empty(cls, user):
        if not cls.get_daily_report(user):
            return False
        return True
