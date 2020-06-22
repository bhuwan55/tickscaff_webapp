from django.urls import path
from .views import index, AddGear, ViewGear, AddJobs, ViewJobs, AddReturned, ViewReturned

urlpatterns = [
    path('', index, name="index_page"),

    path('add-gear/', AddGear, name="add_gear"),
    path('view-gear/', ViewGear, name="view_gear"),

    path('add-jobs/', AddJobs, name="add_jobs"),
    path('view-jobs/', ViewJobs, name="view_jobs"),

    path('return-jobs/<int:id>/', AddReturned, name="return_jobs"),
    path('view-return-jobs/<int:id>/', ViewReturned, name="view_return_jobs"),

]
