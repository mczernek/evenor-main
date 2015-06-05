from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from database.models import Event, Comment


def index(request):
    event_list = Event.objects.order_by('event_name')[:5]
    template = loader.get_template('database/events_list.html')
    context = RequestContext(request, {
        'event_list': event_list,
    })
    return HttpResponse(template.render(context))


def event(request, event_id):
    event = Event.objects.get(id=event_id)
    comment_list = Comment.objects.filter(event_id = event_id).select_related('user')
    context = {'event': event,
               'comment_list': comment_list}
    return render(request, 'database/event_detail.html', context)