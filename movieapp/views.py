from django.http import HttpResponse
from django.shortcuts import render, redirect , get_object_or_404

from .forms import MovieForm
from .models import Movie


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }

    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movie})


def add_movie(request):
    context={}
    if request.method == 'GET':
        context['form'] = MovieForm()
        return render(request , 'add.html' , context)
    
    elif request.method == 'POST':
        form = MovieForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        context['form'] = form
        return render(request , 'add.html' , context)


        

def update(request, id):
    context={}
    movieByid = get_object_or_404(Movie,pk=id)
    if request.method == 'GET':   
        context['form'] = MovieForm(instance=movieByid)
        return render(request , 'edit.html' ,context)

    elif request.method == 'POST':
        formUpdate = MovieForm(request.POST , request.FILES , instance=movieByid)
        if formUpdate.is_valid():
            formUpdate.save()
            return redirect('/')
    else:
        print(formUpdate.errors)
        context['form'] = formUpdate
        return render(request , 'edit.html' ,context)





def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')

