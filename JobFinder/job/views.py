from django.shortcuts import render, redirect
from .models import User
from .models import JobPost


# Create your views here.
def index(request):
    users = User.objects.all()
    jobs = JobPost.objects.all()
    if users is not None:
        for user in users:
            print(user.name)
    return render(request, 'index.html', { 'jobs': jobs })

def jobPost(request):

    experience_level = JobPost.EXPERIENCE_LEVEL_CHOICES
    employment_type = JobPost.EMPLOYMENT_TYPE_CHOICES

    if request.method == 'POST':
        title = request.POST.get('title')
        recruiter = request.POST.get('recruiter')
        description = request.POST.get('description')
        required_skills = request.POST.get('required_skills')
        employment_type = request.POST.get('employment_type')
        experience_level = request.POST.get('experience_level')
        salary_min = request.POST.get('salary_min')
        salary_max = request.POST.get('salary_max')
        location = request.POST.get('location')
        remote_available = request.POST.get('remote_available')
        recruiter = request.POST.get('recruiter')
        application_deadline = request.POST.get('application_deadline')
        active = request.POST.get('is_active')
        if active == 'on':
            is_active = True
        else:
            is_active = False
        job_post = JobPost( title=title, description=description, required_skills=required_skills, employment_type=employment_type, experience_level=experience_level, salary_min=salary_min, salary_max=salary_max, location=location, remote_available=remote_available, recruiter=recruiter, application_deadline=application_deadline, is_active=is_active)
        job_post.save()

        return redirect('index')
    for value, label in experience_level:
        print(value, label)
    return render(request, 'jobPost.html', { 'experience_level': experience_level, 'employment_type': employment_type })

def user_register(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        location = request.POST.get('location')
        role = request.POST.get('role')
        if password == password2:
           user = User(role=role, name=name, username=username, email=email, phone=phone, password=password, location=location)
           user.save()
           return redirect('index')
    return render(request, 'user_register.html')