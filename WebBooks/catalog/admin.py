from django.contrib import admin

from .models import Author, Book, Genre, Language, Status, Bookinstance

#admin.site.register(Author)
# Определения к классу администратор
class AuthorAdmin(admin.ModelAdmin): pass
# Зарегистрируйте класс admin с соответствующей моделью

admin.site.register(Author, AuthorAdmin)
# Регистрируем классы администратора для книг
class AuthorAdmin(admin.ModelAdmin):
      list_display = ("first_name", "last_name", "date_of_birth", "date_of_death")





#admin.site.register(BookInstance)
# Регистрируем классы администратора для экземпляра книги
#@admin.register(Bookinstance)
#class BookinstanceAdmin(admin.ModelAdmin):
 #  pass

@admin.register(Bookinstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'inv_nom')}),
        ('Availability', {'fields': ('status', 'due_back', 'borrower')}),
    )
    pass



class Booksinstanceinline(admin.TabularInline):
    model = Bookinstance



#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    inlines = [Booksinstanceinline]



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass



admin.site.register(Language)
admin.site.register(Status)

# Register your models here.
