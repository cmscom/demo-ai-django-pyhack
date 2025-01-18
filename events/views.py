from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, EventParticipation
from .forms import EventForm, UserRegistrationForm

def event_list(request):
    events = Event.objects.all().order_by('-event_date')
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    participants = event.participants.all()
    is_participant = request.user.is_authenticated and event.participants.filter(id=request.user.id).exists()
    return render(request, 'events/event_detail.html', {
        'event': event,
        'participants': participants,
        'is_participant': is_participant
    })

@login_required
def event_participate(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if not EventParticipation.objects.filter(event=event, participant=request.user).exists():
        EventParticipation.objects.create(event=event, participant=request.user)
        messages.success(request, 'イベントへの参加が完了しました')
    return redirect('event_detail', event_id=event.id)

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'ユーザー登録が完了しました')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'events/user_register.html', {'form': form})

