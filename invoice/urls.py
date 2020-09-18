from django.urls import path
from .views import CreateInvoice, ViewSingleInvoice, ViewAllInvoice, EditInvoice, FinalInvoice

app_name = 'invoice'


urlpatterns = [
    path('create/<int:id>/', CreateInvoice, name="create_invoice"),
    path('view/single/<int:id>', ViewSingleInvoice, name="view_single_invoice"),
    path('view/final/<int:id>', FinalInvoice, name="final_invoice"),
    path('edit/<int:id>', EditInvoice, name="edit_invoice"),
    path('view/all/', ViewAllInvoice, name="view_all_invoice"),

]