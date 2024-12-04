from django.shortcuts import render, redirect

from .models import Person


def home(request):
    return render(request, 'index.html')

def person_list(request):
    people = Person.objects.all()
    ctx = {'people':people}
    return render(request, 'people/list.html', ctx)