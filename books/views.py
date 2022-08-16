from django.views import generic

from .models import Book
class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    

class DetailListView(generic.DetailView):
    model = Book 
    template_name = 'books/book_detail.html'
