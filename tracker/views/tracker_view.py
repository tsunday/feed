import abc

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from tracker.app_services.feed_tracker import FeedTrackerService


@method_decorator(login_required, name='dispatch')
class TrackerView(TemplateView):
    template_name = 'tracker/tracker.html'
    extra_context = {
        'start_api_url': reverse_lazy('tracker:start'),
        'stop_api_url': reverse_lazy('tracker:stop')
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'last_event': FeedTrackerService.get_last_event(user=self.request.user)
        })
        return context


class TrackerApi(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle_request(self, request):
        pass

    def post(self, request):
        try:
            self.handle_request(request)
        except Exception as e:
            return Response({'error': repr(e)}, status=500)
        return Response(status=200)


class StartView(TrackerApi, APIView):
    def handle_request(self, request):
        FeedTrackerService.start_event(request.user)


class StopView(TrackerApi, APIView):
    def handle_request(self, request):
        FeedTrackerService.stop_event(request.user)
