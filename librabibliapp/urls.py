from django.contrib import admin
from django.urls import path
from .views import LibraryView
from .views import LibraryAddView
from .views import LibraryEditView
from .views import LibraryDeleteView
from .views import OrderView

urlpatterns = [
    path('', LibraryView.as_view()),
    path('/<int:pk>', LibraryView.as_view())
    path('create/', LibraryAddView.as_view()),
    path('edit/int<id>', LibraryEditView.as_view()),
    path('delete/int<id>', LibraryDeleteView.as_view()),
    path('order', OrderView.as_view())
]