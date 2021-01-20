from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances =  BookInstance.objects.all().count()
    num_genres = Genre.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Available comedy
    num_genre_comedy = Genre.objects.filter(name='comedy').count() #comedy is 1

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
        'num_genres' : num_genres,
        'num_genre_comedy' : num_genre_comedy,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

#이게 다라고? generic으로 불러오면 저 한 줄이 끝?
from django.views import generic

class BookListView(generic.ListView):
    model =  Book

# 레코드가 없으면 자동으로 404페이지 호출. 
class BookDetailView(generic.DetailView):
    model = Book
