from django.urls import path

from tracker.views.event_list_view import FeedEventListView
from tracker.views.tracker_view import TrackerView, StartView, StopView

app_name = 'tracker'
urlpatterns = [
    path('', TrackerView.as_view(), name='tracker'),
    path('start/', StartView.as_view(), name='start'),
    path('stop/', StopView.as_view(), name='stop'),
    path('event_list/', FeedEventListView.as_view(), name='event_list')
]
