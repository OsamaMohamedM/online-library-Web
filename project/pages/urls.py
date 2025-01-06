from django.urls import path # type: ignore
from .import views
from django.conf.urls.static import static # type: ignore
from django.conf import settings# type: ignore


urlpatterns = [
    path('', views.library,name='library.html'),
    path('sign.html', views.sign,name='sign.html'),
    path('signup.html/', views.signup,name='signup.html'),
    path('main_user.html/', views.main_user,name='main_user.html'),
    path('main_admin.html/', views.main_admin,name='main_admin.html'),
    path('Add-book.htm/', views.AddBook,name='addbook.html'),
    path('delete-book.htm/', views.delete,name='delete.html'),
    path('BorrowBook.html/', views.borrow,name='borrow.html'),
    path('borrowed_books.html/', views.borrowed,name='borrowed.html'),
    path('bookDetails.html/', views.bookDetails,name='bookDetails.html'),
    path('borrowUser.html/', views.borrowUser,name='borrowUser.html'),
    path('search_books/', views.search_books, name='search_books'),
    path('search_book/', views.search_book, name='search_book'),


    path('Edit-book.htm/', views.edit,name='Edit.html'),
    path('Edit.html/', views.Edit, name='Edit'),

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)