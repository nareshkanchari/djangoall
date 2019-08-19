from django.contrib import admin

from .models import Publisher,Author,Student,Book

class AdminPublisher(admin.ModelAdmin):
    list_display = ['publisher_name','publisher_email']
class AdminAuthor(admin.ModelAdmin):
    list_display = ['author_name','author_loc']
class AdminStudent(admin.ModelAdmin):
    list_display = ['student_name','fee']
class AdminBook(admin.ModelAdmin):
    list_display = ['book_name','cost']

admin.site.register(Publisher,AdminPublisher)
admin.site.register(Author,AdminAuthor)
admin.site.register(Student,AdminStudent)
admin.site.register(Book,AdminBook)
