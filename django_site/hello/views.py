#./manage.py runserver
#http://127.0.0.1:8000/hello/
#./manage.py makemigrations
#./manage.py migrate
#dz: car = Cars.objects.first()
# Comment.objects.create(text='sdsfx',car=car)








from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Cars, Comment
from .forms import CommentForm, CarForm
from django.http import HttpResponseRedirect



def expensive_cars(request):
    cars = Cars.objects.filter(price__gte=10000)
    return render(request, 'index.html', {'title': 'hello', 'message': 'CARS', 'cars': cars})


def color_cars(request,color):
    cars = Cars.objects.filter(color=color)
    return render(request, 'index.html', {'title': 'hello', 'message': 'cars', 'cars': cars})


def mark_cars(request,mark):
    cars = Cars.objects.filter(mark=mark)
    return render(request, 'index.html', {'title': 'hello', 'message': 'cars', 'cars': cars})


def model_cars(request,model):
    cars = Cars.objects.filter(model=model)
    return render(request, 'index.html', {'title': 'hello', 'message': 'cars', 'cars': cars})


def add_car(request):
    if request.method == 'GET':
        form = CarForm()
    if request.method == 'POST':
        form = CarForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cars')
    return render(request, 'add.html', {'form': form})



def car(request,id):
    car = get_object_or_404(Cars,id=id)
    comments = car.comment_set.all()
    form = None
    if request.method == 'GET':
        form = CommentForm(initial={'car': car})
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.car_id = id
        if form.is_valid():
            form.save()
    return render(request, 'show.html', {'comments': comments, 'car': car,'form': form})


def cars_color_mark(request,color,mark):
    cars = Cars.objects.filter(color=color,mark=mark)
    return render(request, 'index.html', {'title': 'hello', 'message': 'cars', 'cars': cars})