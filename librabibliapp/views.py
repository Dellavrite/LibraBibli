from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from .models import *
from .forms import BookForm


class LibraryView(View):

    def get(self, request):
        books = Book.objects.all()
        categories = Category.objects.all()
        return render(request, 'index.html', {'books': books, 'categories': categories})


class LibraryAddView(View):

    def get(self, request):
        form = BookForm
        return render(request, 'create.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect("/")
        return self.get(request)



class LibraryEditView(View):

    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        form = BookForm(instance=book)
        return render(request, 'create.html', {'form': form})
