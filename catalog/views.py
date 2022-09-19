from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, Bookinstance, Genre
from django.views import generic
from django.views.generic import ListView, DetailView
from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import *
from django.shortcuts import render
from .forms import AuthorsForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('blyadbook')
    template_name = "book_form.html"

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('blyadbook')
    template_name = "book_form.html"

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('blyadbook')
    template_name = "book_confirm_delete.html"

# получение данных из БД и загрузка шаблона authors_add.html
def authors_add(request):
        allauthor = Author.objects.all()
        authorsform = AuthorsForm()
        return render(request, "catalog/authors_add.html", {"form": authorsform, "allauthor": allauthor})


# Listing 10.28
# сохранение данных об авторах в БД
def create(request):
     if request.method == "POST":
            author = Author()
            author.first_name = request.POST.get("first_name")
            author.last_name = request.POST.get("last_name")
            author.date_of_birth = request.POST.get("date_of_birth")
            author.date_of_death = request.POST.get("date_of_death")
            author.save()
            return HttpResponseRedirect("/authors_add/")


# Listing 10.29
# удаление авторов из БД
def delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/authors_add/")
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Автор не найден</h2>")


# Listing 10.30
# изменение данных в БД
def edit1(request, id):
    error = ""
    author = Author.objects.get(id=id)


    if request.method == "POST":
            author.first_name = request.POST.get("first_name")
            author.last_name = request.POST.get("last_name")
            author.date_of_birth = request.POST.get("date_of_birth")
            author.date_of_death = request.POST.get("date_of_death")
            if author.date_of_birth != "" and author.date_of_death != "":
                author.save()
                return HttpResponseRedirect("/authors_add/")
            else:
                # return HttpResponse("Заполните поля с датами")
                #messages.error(request, 'username or password not correct')
                error = "Заполните поля с датами"
                return render(request, "catalog/edit1.html", {"author": author, "error": error})
    else:
        return render(request, "catalog/edit1.html", {"author": author, "error": error})





class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Универсальный класс представления списка книг,
    находящихся в заказе у текущего пользователя.
    """
    model = Bookinstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')


class BookListView(ListView):
        model = Book
        template_name = 'catalog/book_list1.html'
        paginate_by = 3
        #context_object_name = 'Book'

class MyBookDetailView(DetailView):
      model = Book
     # pk_url_kwarg = "id"
      template_name = 'catalog/My_book_detail.html'
      context_object_name = 'My_book'


class AuthorListView(ListView):
    model = Author
    paginate_by = 4

# Create your views here.
#def index(request):
 #   return HttpResponse("Глaвнaя страница сайта Мир книг!")

#def test(request):
 #    book_title = Book.title
  #   return render(request, 'book_detail.html', context = {'book_title': book_title}
#                        )

def huinana(request):
    return 1



def book_list_view(request):
        book_list=Book.objects.all()
        return render(request, "book_list.html", context = {'book_list': book_list}, )

def show_book(request, id):
    try:
        book = Book.objects.get(id=id)
        book_title = book.title
        return render(request, "book_detail.html", {"book_title": book_title})
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2> не найден</h2>")

def My_admin(request):
       return admin.site.urls

def index(request):
    #Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = Bookinstance.objects.all().count()
    # Доступные книги (статус= 'На складе')
    # Здесь метод 'all()' применен по умолчанию.
    num_instances_available = Bookinstance.objects.filter(status__exact=2).count()
    # Авторы книг,
    num_authors = Author.objects.count()
    # Отрисовка НТМL-шаблона index.html с данными
    # внутри переменной context
    SESSION_SAVE_EVERY_REQUEST = True
    # Количество посещений этого view, подсчитанное
    # в переменной session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'index.html',
                            context={'num_books': num_books,
                                     'num_instances': num_instances,
                                     'num_instances_available': num_instances_available,
                                     'num_authors': num_authors,
                                     'num_visits':num_visits},
                 )


