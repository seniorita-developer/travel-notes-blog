from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Destination, Entry
from .forms import DestinationForm, EntryForm


def index(request):
    return render(request, 'travel_notes_app/index.html')


def destinations(request):
    """Showing only destinations of this particular user"""
    destination_list = Destination.objects.order_by('date_added')
    # destination_list = Destination.objects.filter(owner=request.user).order_by('date_added')
    context = {'destinations': destination_list}
    return render(request, 'travel_notes_app/destinations.html', context)


def destination(request, dest_id):
    dest = Destination.objects.get(id=dest_id)

    entries = dest.entry_set.order_by('-date_added')
    context = {'destination': dest, 'entries': entries}
    return render(request, 'travel_notes_app/destination.html', context)


@login_required
def new_destination(request):
    if request.method != 'POST':
        # An empty form created
        form = DestinationForm()
    else:
        # Processing data from POST request
        form = DestinationForm(request.POST)
        if form.is_valid():
            new_dest = form.save(commit=False)
            """New entry connecting with user"""
            new_dest.owner = request.user
            new_dest.save()
            return HttpResponseRedirect(reverse('destinations'))

    context = {'form': form}
    return render(request, 'travel_notes_app/new_destination.html', context)


# Add a new note for specific destination
@login_required
def new_entry(request, dest_id):
    dest = Destination.objects.get(id=dest_id)

    if request.method != 'POST':
        # An empty form created
        form = EntryForm()
    else:
        # Processing data from POST request
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.destination = dest
            new_note.owner = request.user
            new_note.save()
            return HttpResponseRedirect(reverse('destination', args=[dest_id]))

    context = {'destination': dest, 'form': form}
    return render(request, 'travel_notes_app/new_entry.html', context)


# Edit existing note
@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    dest = entry.destination
    if dest.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # An empty form created
        form = EntryForm(instance=entry)
    else:
        # Processing data from POST request
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('destination', args=[dest.id]))

    context = {'entry':entry, 'destination': dest, 'form': form}
    return render(request, 'travel_notes_app/edit_entry.html', context)
