from django.shortcuts import render,get_object_or_404
from .models import Author,Book,Category,Member,Borrow
# Create your views here.
def home(request):
    authors = Author.objects.all()
    categories = Category.objects.all()
    total_authors = authors.count()
    total_categories = categories.count()
    total_members = Member.objects.count()
    total_borrowed = Borrow.objects.count()

    context = {
        'authors': authors,
        'categories': categories,
        'total_authors': total_authors,
        'total_categories': total_categories,
        'total_members': total_members,
        'total_borrowed': total_borrowed,
    }

    return render(request, 'store/home.html', context)


def book_details(request,book_id):
    book=get_object_or_404(Book,id=book_id)
    return render(request,'store/book_details.html',{'book':book})
def member_details(request):
    members=Member.objects.all()
    return render(request,'store/member.html',{'members':members})
def borrow(request):
    borrow=Borrow.objects.all()
    return render(request,'store/borrow.html',{'borrows':borrow})


def each_book(request,book_id):
    book=get_object_or_404(Book,id=book_id)
    borrow_count=Borrow.objects.filter(book=book).count()
    context = {
        'book': book,
        'borrow_count': borrow_count
    }
    return render(request,'store/book_details.html',context)
    
def books_by_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(author=author)
    return render(request, 'store/books_list.html', {'books': books, 'title': f"Books by {author.name}"})

def books_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    books = Book.objects.filter(category=category)
    return render(request, 'store/books_list.html', {'books': books, 'title': f"Category: {category.name}"})
