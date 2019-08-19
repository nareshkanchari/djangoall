
from django.db import models

class Publisher(models.Model):
    publisher_name=models.CharField(max_length=50)
    publisher_email=models.EmailField(max_length=50)
    def __str__(self):
        return self.publisher_name

class Author(models.Model):
    author_name=models.CharField(max_length=50)
    author_loc=models.CharField(max_length=50)
    def __str__(self):
        return self.author_name

class Student(models.Model):
    student_name=models.CharField(max_length=50)
    fee=models.IntegerField()
    def __str__(self):
        return self.student_name

class Book(models.Model):
    publisher=models.OneToOneField(Publisher,on_delete=models.CASCADE)
    author=models.ManyToManyField(Author)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    book_name=models.CharField(max_length=50)
    cost=models.IntegerField()
    def __str__(self):
        return self.book_name

