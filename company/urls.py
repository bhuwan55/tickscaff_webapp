from django.urls import path
from .views import AddCompany, ViewCompany, EditCompany, DeleteCompany
app_name = 'company'

urlpatterns = [
    path('add/', AddCompany, name='add_company'),
    path('view/', ViewCompany, name='view_company'),
    path('edit/<int:id>/', EditCompany, name='edit_company'),
    path('delete/<int:id>/', DeleteCompany, name='delete_company'),

]
