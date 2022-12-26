from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    public_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    person_name = models.CharField(label="ФИО")
    phone = models.CharField(label="Номер телефона", widget=forms.NumberInput)
