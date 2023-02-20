from django.shortcuts import render
from .forms import EmployeeCreateForm

# Create your views here.
# def demo(request):
#     context = {
#         "class_name": "Django Class",
#         "date": "2023-02-14",
#         "day": "Tuesday"
#     }

def employee_index(request):
    return render(request, 'employees/index_employee.html')

def employee_add(request):
    emp_create_form = EmployeeCreateForm()
    context = {"form": emp_create_form}
    return render(request, 'employees/add_employee.html', context)

def employee_edit(request):
    return render(request, 'employees/edit_employee.html')
    
def employee_show(request):
    return render(request, 'employees/show_employee.html')

def department_index(request):
    return render(request, 'departments/index_department.html')

def department_add(request):
    return render(request, 'departments/add_department.html')

def department_edit(request):
    return render(request, 'departments/edit_department.html')

def department_show(request):
    return render(request, 'departments/show_department.html')

def salary_record_index(request):
    return render(request, 'salaryrecords/index_salary_record.html')

def salary_record_add(request):
    return render(request, 'salaryrecords/add_salary_record.html')

def salary_record_edit(request):
    return render(request, 'salaryrecords/edit_salary_record.html')

def salary_record_show(request):
    return render(request, 'salaryrecords/show_salary_record.html')