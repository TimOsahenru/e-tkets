from django import forms
from events.models import Event

class EventCreateForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['event_creator']


class EventEditForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['event_creator']