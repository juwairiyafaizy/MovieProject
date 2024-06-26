from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AddForm
from .forms import MovieForm
from .models import Movie


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    # context={
    #     'movie_list':movie
    # }
    return render(request, 'index.html', {'result': movie})


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movie})


def add(request):
    movie1= Movie.objects.all()
    form1 = AddForm(request.POST or None, request.FILES)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request, 'add.html', {'form1': form1, 'movie1': movie1})


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
