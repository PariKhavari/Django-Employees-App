from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date


def employee_overview(request):

    # Hier die entsprechenden Filter anlegen und die context-Variable definieren, um die Daten an das Template zu übergeben

    all_employees = Employee.objects.all()
    employees_over_3000 = Employee.objects.filter(salary__gt=3000)
    count_over_5000 = Employee.objects.filter(salary__gte=5000).count()
    sales_employees = Employee.objects.filter(department__name="Sales")
    average_salary_sales = sales_employees.aggregate(Avg('salary'))
    employee_bevor_2022_not_in_hr = Employee.objects.filter(
        Q(hire_date__lt=date(2022, 1, 10)) & ~Q(department__name='HR'))

    context = {
        'all_employees': all_employees,
        'employees_over_3000': employees_over_3000,
        'count_over_5000': count_over_5000,
        'sales_employees': sales_employees,
        'average_salary_sales': average_salary_sales,
        'employee_bevor_2022_not_in_hr': employee_bevor_2022_not_in_hr,
    }

    return render(request, 'employee_list.html', context)


