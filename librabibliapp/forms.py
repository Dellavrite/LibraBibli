from django import forms
from django.forms import ModelChoiceField, ModelForm

from librabibliapp.models import Book


class OrderForm(forms.Form):
    book = ModelChoiceField(label="Книга", queryset=Book.objects.all(), to_field_name="name")
    person_name = forms.CharField(label="ФИО")
    phone = forms.CharField(label="Номер телефона", widget=forms.NumberInput)

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

