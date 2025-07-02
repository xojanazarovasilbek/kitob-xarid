from django.shortcuts import render
from .models import Books
# Create your views here.


def book_list(request):
    books = Books.objects.all().order_by('-id')
    return render(request, 'kitoblar.html',{'books': books})


def book_detail(request, pk):
    book = Books.objects.get(id=pk)
    return render(request, 'book_detam.html', {'book': book})

