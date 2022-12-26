from django.shortcuts import render
from django.views import View


class LibraryView(View):

     def get(self, request):
         return render(request, 'index.html')


class LibraryAddView(View):

    def get(self, request):
        return render(request, 'create.html')