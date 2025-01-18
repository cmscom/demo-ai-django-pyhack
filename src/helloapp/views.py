from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event
from .forms import ApplicationForm


def hello_world_view(request):
    return HttpResponse("Hello World")


def event_list_view(request):
    events = Event.objects.all().order_by('start_date')
    return render(request, "helloapp/event_list.html", {"events": events})


def event_detail_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "helloapp/event_detail.html", {"event": event})


def application_form_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.event = event
            application.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = ApplicationForm()

    return render(request, 'helloapp/application_form.html', {
        'form': form,
        'event': event,
    })
