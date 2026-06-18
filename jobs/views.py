from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Student, Company, Job, Application
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def home(request):
    students = Student.objects.all()
    companies = Company.objects.all()
    
    search = request.GET.get('search')

    if search:
        jobs = Job.objects.filter(title__icontains=search)
    else:
        jobs = Job.objects.all()
    applications = Application.objects.all()
    total_applications = Application.objects.count()

    context = {
        'students': students,
        'companies': companies,
        'jobs': jobs,
        'applications': applications,
        'total_applications': total_applications,
    }
    return render(
        request,
        'home.html',
        context
    )
@login_required(login_url='/login/')
def apply_job(request, job_id):

    student = Student.objects.filter(
        user=request.user
    ).first()

    if not student:

        messages.error(
            request,
            "You are not eligible to apply for placement drives."
        )

        return redirect('/')

    job = Job.objects.get(id=job_id)

    already_applied = Application.objects.filter(
        student=student,
        job=job
    ).exists()

    if already_applied:

        messages.warning(
            request,
            "You have already applied for this job."
        )

        return redirect('/')

    if request.method == "POST":

        Application.objects.create(
            student=student,
            job=job,
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            skills=request.POST['skills'],
            cover_letter=request.POST['cover_letter']
        )

        messages.success(
            request,
            "Application submitted successfully."
        )

        return redirect('/my-applications/')

    return render(
        request,
        'apply_form.html',
        {
            'job': job,
            'student': student
        }
    )
def add_student(request):

    if request.method == 'POST':

        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            skills=request.POST['skills'],
            cgpa=request.POST['cgpa']
        )

        return redirect('/')

    return render(request, 'student_form.html')
def add_company(request):

    if request.method == "POST":

        Company.objects.create(
            company_name=request.POST['company_name'],
            location=request.POST['location'],
            website=request.POST['website'],
            package=request.POST['package']
        )

        return redirect('/')

    return render(request, 'add_company.html')
def add_job(request):

    companies = Company.objects.all()

    if request.method == "POST":

        company = Company.objects.get(
            id=request.POST['company']
        )

        Job.objects.create(
            company=company,
            title=request.POST['title'],
            salary=request.POST['salary'],
            eligibility=request.POST['eligibility']
        )

        return redirect('/')

    return render(
        request,
        'add_job.html',
        {'companies': companies}
    )
def delete_job(request, job_id):

    job = Job.objects.get(id=job_id)

    job.delete()

    return redirect('/')
def edit_job(request, job_id):

    job = Job.objects.get(id=job_id)

    if request.method == "POST":
        job.title = request.POST['title']
        job.salary = request.POST['salary']
        job.eligibility = request.POST['eligibility']
        job.save()

        return redirect('/')

    return render(request, 'edit_job.html', {'job': job})
def delete_student(request, student_id):

    student = Student.objects.get(id=student_id)

    student.delete()

    return redirect('/')
def edit_student(request, student_id):

    student = Student.objects.get(id=student_id)

    if request.method == "POST":

        student.name = request.POST['name']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.skills = request.POST['skills']
        student.cgpa = request.POST['cgpa']

        student.save()

        return redirect('/')

    return render(
        request,
        'edit_student.html',
        {'student': student}
    )
def delete_company(request, company_id):
    company = Company.objects.get(id=company_id)
    company.delete()
    return redirect('/')
def edit_company(request, company_id):
    company = Company.objects.get(id=company_id)

    if request.method == "POST":
        company.company_name = request.POST['company_name']
        company.location = request.POST['location']
        company.website = request.POST['website']
        company.package = request.POST['package']
        company.save()

        return redirect('/')

    return render(
        request,
        'edit_company.html',
        {'company': company}
    )
def delete_application(request, application_id):
    application = Application.objects.get(id=application_id)

    application.delete()

    return redirect('/')
def signup_user(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            password=password
        )

        Student.objects.create(
            user=user,
            name=username,
            email="",
            phone="",
            skills="",
            cgpa=0
        )

        return redirect('/login/')

    return render(request, 'signup.html')


def login_user(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')
def logout_user(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def my_profile(request):

    student = Student.objects.filter(
        user=request.user
    ).first()
    if not student:

       return render(
        request,
        'my_profile.html',
        {
            'student': None
        }
    )
    
    if request.method == "POST":

        student.name = request.POST['name']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.skills = request.POST['skills']
        student.cgpa = request.POST['cgpa']

        student.save()

        messages.success(
            request,
            "Profile updated successfully."
        )

        return redirect('/my-profile/')

    return render(
        request,
        'my_profile.html',
        {
            'student': student
        }
    )

def shortlist_application(request, application_id):

    application = Application.objects.get(id=application_id)

    application.status = "Shortlisted"

    application.save()

    return redirect('/')


def select_application(request, application_id):

    application = Application.objects.get(id=application_id)

    application.status = "Selected"

    application.save()

    return redirect('/')


def reject_application(request, application_id):

    application = Application.objects.get(id=application_id)

    application.status = "Rejected"

    application.save()

    return redirect('/')

@login_required(login_url='/login/')
def my_applications(request):

    student = Student.objects.filter(
        user=request.user
    ).first()

    if not student:

        messages.error(
            request,
            "You are not eligible for placement applications."
        )

        return redirect('/')

    applications = Application.objects.filter(
        student=student
    )

    return render(
        request,
        'my_applications.html',
        {
            'applications': applications
        }
    )
@login_required(login_url='/login/')
def edit_application(request, application_id):

    application = Application.objects.get(
        id=application_id
    )

    if request.method == "POST":

        application.name = request.POST['name']
        application.email = request.POST['email']
        application.phone = request.POST['phone']
        application.skills = request.POST['skills']
        application.cover_letter = request.POST['cover_letter']

        application.save()

        messages.success(
            request,
            "Application updated successfully."
        )

        return redirect('/my-applications/')

    return render(
        request,
        'edit_application.html',
        {
            'application': application
        }
    )