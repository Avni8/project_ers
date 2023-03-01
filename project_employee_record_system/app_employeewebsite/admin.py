from django.contrib import admin
from .models import Department, Employee

# Register your models here.

class AdminEmployee(admin.ModelAdmin):
    list_display = ("full_name", "joined_date", "email", "contact")
    serach_fiels = ("full_name", "email")
    list_filter = ("full_name", "email")
    

admin.site.register(Department)
admin.site.register(Employee, AdminEmployee)

admin.site.site_header = 'ERS'
admin.site.site_title = 'ERS'
admin.site.index_title =  'Admin Panel'

