from django.contrib import admin

from .models import Customer,Student,Emp

class AdminCustomer(admin.ModelAdmin):
    list_display = ['name','loc','sales']
class AdminEmp(admin.ModelAdmin):
    list_display = ['name','loc','salary']
class AdminStudent(admin.ModelAdmin):
    list_display = ['name','loc','marks']

admin.site.register(Customer,AdminCustomer)
admin.site.register(Emp,AdminEmp)
admin.site.register(Student,AdminStudent)