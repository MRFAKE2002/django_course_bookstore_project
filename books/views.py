from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Book
from .forms import CommentForm
class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    

# class DetailListView(generic.DetailView):
#     model = Book 
#     template_name = 'books/book_detail.html'


# for have " new_comment_user " we need user login and for function we must use decorator
@login_required
# we use function instead of class because of make our custom CommentForm and use it in detail view
def book_detail_view(request, pk):
    # get the book object
    book = get_object_or_404(Book, pk=pk)
    # list of all comments that have been relate with this book 
    book_comments = book.comments.all()
    # get comment of book   
    if request.method == 'POST':
        # make a comment by user request 
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            # get the comment text from user request by CommentForm that has only text field
            new_comment = comment_form.save(commit=False)
            # get the comment book from the page that we fill the CommentForm
            new_comment.book = book
            # get the comment user from the user that login
            new_comment.user = request.user
            # save the comment in database 
            new_comment.save()
            # after get comment from user we get back a empty new CommentForm
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
        
    context = { 'book':book ,
                'comments':book_comments ,
                'comment_form':comment_form,
            }
     
    return render(request, 'books/book_detail.html', context)    


# for have make a new book we need user login and for class we must use mixin class
class BookCreateView(LoginRequiredMixin , generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/book_create.html'
    

class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
