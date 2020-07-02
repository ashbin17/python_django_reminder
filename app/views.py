from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.


def index(request):
    reminder = Reminder.objects.all()
    return render(request, 'index.html', {'reminder': reminder})


def add_reminder(request):
    if request.method == 'POST':
        note = request.POST.get('note')
        date = request.POST.get('date')
        obj = Reminder()
        obj.note = note
        obj.date = date
        obj.save()
    reminder = Reminder.objects.all()
    return render(request, 'index.html', {'reminder': reminder})


def update(request, id):
    rem = Reminder.objects.get(pk=id)
    return render(request, 'update.html', {'rem': rem})


def updating(request, id):
    if request.method == 'POST':
        note = request.POST.get('note')
        date = request.POST.get('date')
        Reminder.objects.filter(pk=id).update(note=note, date=date)
    reminder = Reminder.objects.all()
    return render(request, 'index.html', {'reminder': reminder})


def delete(request, id):
    Reminder.objects.filter(pk=id).delete()
    reminder = Reminder.objects.all()
    return render(request, 'index.html', {'reminder': reminder})