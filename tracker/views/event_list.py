from django.views.generic import ListView

from tracker.models.feed_event import FeedEvent


class FeedEventListView(ListView):
    model = FeedEvent
    template_name = 'tracker/event_list.html'