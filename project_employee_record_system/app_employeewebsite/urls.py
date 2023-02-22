from django.urls import path
from . import views 
urlpatterns = [
    path('employees/', views.employee_index, name='emp-index'),
    path('employees/show/<int:id>/', views.employee_show, name='emp-show'),
    path('employees/edit/<int:id>/', views.employee_edit, name='emp-edit'),
    path('employees/delete/<int:id>/', views.employee_delete, name='emp-delete'),
    path('employees/add/', views.employee_add, name='emp-add'),

    path('departments/', views.department_index, name='dept-index'),
    path('departments/show/', views.department_show, name='dept-show'),
    path('departments/edit/', views.department_edit, name='dept-edit'),
    path('departments/add/', views.department_add, name='dept-add'),

    path('salaryrecords/', views.salary_record_index, name = 'salary-index'),
    path('salaryrecords/show/', views.salary_record_show, name='salary-show'),
    path('salaryrecords/edit/', views.salary_record_edit, name='salary-edit'),
    path('salaryrecords/add/', views.salary_record_add, name = 'salary-add')

]
