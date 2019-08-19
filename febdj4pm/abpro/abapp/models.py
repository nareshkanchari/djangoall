from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=50)
    loc = models.CharField(max_length=50)
    class Meta:
        abstract = True

class Customer(Data):

    sales = models.IntegerField()
    def __str__(self):
        return self.name

class Emp(Data):
    salary = models.IntegerField()
    def __str__(self):
        return self.name

class Student(Data):
    marks = models.IntegerField()
    def __str__(self):
        return self.name