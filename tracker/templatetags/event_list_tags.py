from django import template

from tracker.app_services.feed_tracker import FeedTrackerService

register = template.Library()


@register.inclusion_tag('tracker/event_list_link.html')
def show_event_list_link(user):
    return {
        'active': FeedTrackerService.is_daily_report_empty(user)
    }
