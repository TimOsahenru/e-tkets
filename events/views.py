from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from events.forms import EventCreateForm, EventEditForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from events.models import Event


def home_page(request):
    events = Event.objects.all()[:3]

    return render(request, 'index.html', {'events': events})


@login_required(login_url='login')
def create_event(request):
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.event_creator = request.user
            event.save() #unittest this
            return redirect('profile')

    else:
        form = EventCreateForm()

    return render(request, 'create-event.html', {'form': form, 'active_page': 'create_event'})


@login_required
def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if event.event_creator != request.user:
        return redirect('profile')
    
    if request.method == 'POST':
        form = EventEditForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EventEditForm(instance=event)
    return render(request, 'edit-event.html', {'form': form, 'event': event, 'active_page': 'edit_event'})



@login_required
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if event.event_creator != request.user:
        return redirect('profile')
    
    if request.method == 'POST':
        event.delete()
        return redirect('profile')
    
    return render(request, 'delete-event.html', {'event': event, 'active_page': 'event_delete'})

