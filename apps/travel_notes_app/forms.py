from django import forms

from .models import Destination, Entry


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['text']
        labels = {'text':''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

