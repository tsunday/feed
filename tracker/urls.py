from django.urls import path

from tracker.views.tracker_view import TrackerView, StartView, StopView

app_name = 'tracker'
urlpatterns = [
    path('/', TrackerView.as_view(), name='tracker'),
    path('/start/', StartView.as_view(), name='start'),
    path('/stop/', StopView.as_view(), name='stop'),
]
