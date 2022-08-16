from django.urls import path

from . import views


urlpatterns= [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.DetailListView.as_view(), name='book_detail'),
    path('new/', views.BookCreateView.as_view(), name='book_create')
]
