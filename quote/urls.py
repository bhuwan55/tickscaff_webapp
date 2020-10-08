from django.urls import path
from .views import CreateQuote, ViewSingleQuote, ViewAllQuote, EditQuote, DeleteQuote, Sendmail

app_name = 'quote'


urlpatterns = [
    path('create/', CreateQuote, name="create_quote"),
    path('view/all', ViewAllQuote, name="view_all_quote"),
    path('view/single/<int:id>', ViewSingleQuote, name="view_single_quote"),
    path('edit/<int:id>', EditQuote, name="edit_quote"),
    path('delete/<int:id>', DeleteQuote, name="delete_quote"),

    path('send/<int:id>', Sendmail, name="send_mail"),

    ]