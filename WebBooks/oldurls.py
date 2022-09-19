from django.contrib import admin
from django.urls import path
from catalog import views
from django.db import models
#from catalog\models import Book, Author, Bookinstance, Genre


#from . import views
#from .views import *

#from django.conf.urls import url - url заменена re_path с версии 4.0 django
from django.urls import re_path

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    #path('books/<int:id>/', views.show_book),

    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    #booklistview должна вызывать get_absolute_url из модели данных. которая должна возвращать
    #pk для bookdetailview. По факту не возвращает
    #re_path(r'^books/$', views.book_list_view, name='books'),

    #path('books/', views.book_list_view, name='books'),
   # path('test/', views.test, name='book_detail'),

    #re_path(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    #поэтому приходится использовать определить вручную фунцию book_list_view
    #где берем аргумент id книги. Чтобы bookdetailview получил свой любимый pk
    #в BookDetailView прописываем pk_url_kwarg = "id"

    path('books/show_book/<int:id>/', views.show_book),
   # path('books/<int:id>/', views.show_book),

]



#urlpatterns = [
 #   path('', views.index, name='index'),
 #]

