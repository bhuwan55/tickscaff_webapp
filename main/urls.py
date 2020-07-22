from django.urls import path
from .views import Login,NewAddJobs, index, AddGear, ViewGear, AddJobs, AddGearNumber, ViewJobs, AddReturned, ViewReturned, EditGear, DeleteGear, EditJobs, DeleteJobs
from django.contrib.auth import views as auth_views
app_name = 'main'


urlpatterns = [
    path('',Login, name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),

    path('index', index, name="index_page"),

    path('add-gear/', AddGear, name="add_gear"),
    path('view-gear/', ViewGear, name="view_gear"),
    path('edit-gear/<int:id>', EditGear, name="edit_gear"),
    path('delete-gear/<int:id>', DeleteGear, name="delete_gear"),
    path('add-update-gear/', AddGearNumber, name="add-update-gear"),

    path('add-jobs/', AddJobs, name="add_jobs"),
    path('view-jobs/', ViewJobs, name="view_jobs"),
    path('edit-jobs/<int:id>', EditJobs, name="edit_jobs"),
    path('delete-jobs/<int:id>', DeleteJobs, name="delete_jobs"),
    path('new-add-jobs/<int:id>', NewAddJobs, name="new_add_jobs"),

    path('return-jobs/<int:id>/', AddReturned, name="return_jobs"),
    path('view-return-jobs/<int:id>/', ViewReturned, name="view_return_jobs"),

]
