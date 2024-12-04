from django.shortcuts import render, redirect, get_object_or_404

from .models import Person


def home(request):
    return render(request, 'index.html')


def person_list(request):
    people = Person.objects.all()
    ctx = {'people': people}
    return render(request, 'people/list.html', ctx)


def person_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        job_title = request.POST.get('job_title')
        address = request.POST.get('address')
        if (first_name and last_name and
                age and address and job_title):
            Person.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                job_title=job_title,
                address=address
            )
            return redirect('people:list')
    return render(request, 'people/form.html')


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    ctx = {'person':person}
    return render(request, 'people/detail.html', ctx)


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('people:list')
