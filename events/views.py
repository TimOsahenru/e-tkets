from django.shortcuts import render, redirect
from django.http import HttpResponse
from events.forms import EventCreateForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def create_event(request):
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EventCreateForm()

    return render(request, 'create-event.html', {'form': form})