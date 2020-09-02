from django.shortcuts import render
from .models import Movie
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

# Create your views here.
def homepage(request):
    movies = Movie.objects.all()
    query = request.GET.get("q")
    if query:
        movies = movies.filter(
            Q(name__icontains=query)
        ).distinct()
    return render(request, 'mainpage/index.html', {'movies': movies})