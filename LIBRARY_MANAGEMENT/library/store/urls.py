from django.urls import path
from .views import borrow,home,member_details,books_by_author,books_by_category
urlpatterns=[
    path("",home,name="author"),
    path('borrows/', borrow, name='borrow'),
    path('members/', member_details, name='member_details'),
    # urls.py
    path('book_author/<int:author_id>/', books_by_author, name='books_by_author'),

    path('book_category/<int:category_id>/',books_by_category,name='books_by_category')

]