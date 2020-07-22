from django.urls import path
from .views import AddEmployee, ViewEmployee, ViewSingleEmployee, DeleteEmployee, DeleteWork, ChangeMonth, ResetTotalHours, EditWork
app_name = 'employee'

urlpatterns = [
    path('add/', AddEmployee, name='add_employee'),
    path('view/', ViewEmployee, name='view_employee'),
    path('view/single/<int:id>', ViewSingleEmployee, name='view_single_employee'),
    path('delete/<int:id>', DeleteEmployee, name='delete_employee'),

    path('delete/work/<int:id>', DeleteWork, name='delete_work'),
    path('edit/work/<int:id>', EditWork, name='edit_work'),

    path('change/month/<int:id>', ChangeMonth, name='change_month'),

    path('reset/total_hours/<int:id>', ResetTotalHours, name='reset_total_hours'),

]
