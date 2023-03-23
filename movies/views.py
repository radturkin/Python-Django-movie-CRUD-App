from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

def movies(request):
   data = Movie.objects.all()
   return render(request, "movies/movies.html", {'movies':data})
    
def home(request):
    return HttpResponse("home page")

def detail(request, id):
   data = Movie.objects.get(pk=id)
   return render(request, 'movies/details.html', {'movie':data})

def add(request):
   title = request.POST.get('title')
   year =  request.POST.get('year')
   
   if title and year:
      movie = Movie(title=title, year=year)
      movie.save()
      return HttpResponseRedirect("/movies")
   return render(request, 'movies/add.html')

def delete(request, id):
   try:
      movie=Movie.objects.get(pk=id)
   except: 
      raise Http404("no such movie")
   movie.delete()
   return HttpResponseRedirect("/movies")