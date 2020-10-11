from django.urls import path
from .views import CreateInvoice, ViewSingleInvoice, ViewPdfInvoice, ViewAllInvoice, DeleteInvoice, EditInvoice, FinalInvoice, CreateNewInvoice, Sendmail

app_name = 'invoice'


urlpatterns = [
    path('create/<int:id>/', CreateInvoice, name="create_invoice"),
    path('view/single/<int:id>', ViewSingleInvoice, name="view_single_invoice"),
    path('view/final/<int:id>', FinalInvoice, name="final_invoice"),
    path('edit/<int:id>', EditInvoice, name="edit_invoice"),
    path('view/all/', ViewAllInvoice, name="view_all_invoice"),
    path('create/new/', CreateNewInvoice, name="create_new_invoice"),
    path('delete/<int:id>', DeleteInvoice, name="delete_invoice"),

    path('send/<int:id>', Sendmail, name="send_mail"),
    path('view/<int:id>', ViewPdfInvoice, name="view_pdf")

]