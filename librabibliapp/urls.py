from django.contrib import admin
from django.urls import path
from .views import LibraryView
from .views import LibraryAddView
from .views import LibraryEditView


from .views import LibraryDeleteView

urlpatterns = [
    path('', LibraryView.as_view()),
    path('create/', LibraryAddView.as_view()),
    path('edit/int<id>', LibraryEditView.as_view()),
    path('delete/int<id>', LibraryDeleteView.as_view()),
]