from django.contrib import admin
from django.urls import path
from jobs.views import delete_application
from jobs.views import delete_company,edit_company
from jobs.views import home, apply_job, add_student, add_company, add_job, delete_job,edit_job, delete_student, edit_student
from jobs.views import signup_user, login_user
from jobs.views import logout_user
from jobs.views import my_applications
from jobs.views import edit_application

from jobs.views import (
    shortlist_application,
    select_application,
    reject_application
)
from jobs.views import my_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('apply/<int:job_id>/', apply_job),
    path('add-student/', add_student),
    path('add-company/', add_company),
    path('add-job/', add_job),
    path('delete-job/<int:job_id>/', delete_job),
    path('edit-job/<int:job_id>/', edit_job),
    path('delete-student/<int:student_id>/', delete_student),
    path(
    'edit-student/<int:student_id>/',
    edit_student
),
path(
    'delete-company/<int:company_id>/',
    delete_company
),

path(
    'edit-company/<int:company_id>/',
    edit_company
),
path(
    'delete-application/<int:application_id>/',
    delete_application
),
path('signup/', signup_user),
path('login/', login_user),
path('logout/', logout_user),
path('my-profile/', my_profile),
path(
    'shortlist/<int:application_id>/',
    shortlist_application
),

path(
    'select/<int:application_id>/',
    select_application
),

path(
    'reject/<int:application_id>/',
    reject_application
),
path(
    'my-applications/',
    my_applications
),
path(
    'edit-application/<int:application_id>/',
    edit_application
),
]