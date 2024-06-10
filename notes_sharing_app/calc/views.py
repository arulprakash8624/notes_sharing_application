from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User  # Import Django's built-in User model
from .models import Student, Staff,files

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request,'login.html')
# def staff(request):
#     return render(request,'staff.html')
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            #login(request, user)
            if user.is_staff==True:
                staff = Staff.objects.filter(email=user.email)
                id=staff[0]
                file= files.objects.filter(staff_id=id.staff_id).values()
                return render(request,'staff.html',{'staff':staff,'files':file})
            elif user.is_staff==False:
                student = Student.objects.filter(email=user.email).values()
                notes= files.objects.all().values()
                return render(request,'student.html',{'student':student,'notes':notes})
            else:
                return render(request, 'login.html', {'error_message': user.is_staff})
        else:
            error_message = 'Invalid email or password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        if request.user.is_authenticated:
            if hasattr(request.user, 'staff'):
                return redirect('staff.html')
            elif hasattr(request.user, 'student'):
                return redirect('student.html')
            else:
                return redirect('result.html')
        else:
            return render(request, 'login.html')

    # Add a default return statement
    return redirect('login.html')  # Redirect to login page if none of the conditions are met

def result(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        return render(request, 'result.html', {'result': email})
    else:
        return HttpResponse('Invalid request')

def submit_registration(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_type = request.POST.get('userType')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        # Check if the email is already used
        if User.objects.filter(email=email).exists():
            return HttpResponse('Email already exists')
        
        # Create a new user
       
        
        # Assign user to either student or staff based on the user_type
        if user_type == 'student':
            register_number = request.POST.get('registerNumber')
            year = request.POST.get('year')
            dept = request.POST.get('dept')
            section = request.POST.get('section')
            student = Student.objects.create(email=email,register_number=register_number, year=year, dept=dept, section=section,username=email,first_name=first_name,last_name=last_name)
            student.save()
            user = User.objects.create_user(email, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        elif user_type == 'staff':
            staff_id = request.POST.get('staffId')
            position = request.POST.get('position')
            staff = Staff.objects.create(email=email,is_staff=1,staff_id=staff_id, position=position,username=email,first_name=first_name,last_name=last_name)
            staff.save()
            user = User.objects.create_user(email,email, password,is_staff=1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        
        return render(request,'result.html')
    else:
        return HttpResponse('Invalid request')

def upload(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        file = request.FILES.get('file')  # Retfilerieve file data from request.FILES
        staff_id=request.POST.get('staff_id')
        
        if file:  # Ensure a file was provided
            new_file = files.objects.create(name=name, files=file,staff_id=staff_id)
            new_file.save()
            staff = Staff.objects.filter(staff_id=staff_id)
            files_list = files.objects.filter(staff_id=staff_id).values()
            return render(request, "staff.html", {'staff':staff,"files": files_list})
        else:
            return HttpResponse("No file provided")
    else:
        return HttpResponse("Invalid request method")
def delete(request):
    if request.method=='POST':
        id=request.POST.get('id')
        staff_id=request.POST.get('staff_id')
        file=files.objects.get(id=id)
        file.delete()
        staff = Staff.objects.filter(staff_id=staff_id)
        files_list = files.objects.filter(staff_id=staff_id).values()
        return render(request, "staff.html", {'staff':staff,"files": files_list})
