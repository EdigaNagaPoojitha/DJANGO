from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()  # long text is fine here

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)  # better than TextField

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)  # better than TextField
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)  # better: no duplicate emails

    def __str__(self):
        return self.name


class Borrow(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrows')
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrows')

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"
