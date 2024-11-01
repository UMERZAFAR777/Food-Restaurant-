from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from info.models import Profile
from New_Menu.models import New_Menu,Section
from custom_birthday.models import Custom_Birthday
from chef.models import Chef
from birthday_table.models import Custom_Table
from django.conf import settings
from django.core.mail import send_mail
from gallery.models import Gallery







def index(request):
    menu = New_Menu.objects.all()
    section = Section.objects.prefetch_related('new_menu_set')
    birthday = Custom_Birthday.objects.all()
    chef = Chef.objects.all()
    img = Gallery.objects.all()

    
    data = {
        'menu': menu,
        'section': section,
        'birthday': birthday,
        'chef': chef,
        'img':img,
    }
    return render(request, 'index.html', data)

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, "Incorrect Email/Password")  
#             return redirect('login')
#     return render(request, 'login.html')
from django.contrib import messages, auth

from django.contrib.auth.models import User
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Debugging to check if data is received
        print(f"Received Email: {email}, Password: {password}")
        
        try:
            # Retrieve user based on email
            user = User.objects.get(email=email)
            # Authenticate using the user's username and password
            user = auth.authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None
        
        if user is not None:
            # Successful login
            auth.login(request, user)
            return redirect('index')
        else:
            # Failed login attempt
            messages.error(request, "Incorrect Email/Password")
            return redirect('login')
    
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname') 
        lastname = request.POST.get('lastname')    
        phone = request.POST.get('phone')          
        email = request.POST.get('email')         
        password = request.POST.get('password')    
        password1 = request.POST.get('password1') 
        gender = request.POST.get('gender')        

        # Check if all fields are filled
        if not firstname or not lastname:
            messages.error(request, 'First name and last name are required!')
            return redirect('register')

        # Check if passwords match
        if password != password1:
            messages.error(request, 'Both passwords do not match...!')
            return redirect('register')

        try:
            # Create user
            user = User.objects.create_user(username=email.split('@')[0], email=email, password=password)
            user.save()

            # Store additional user info (like firstname, lastname, phone, gender)
            # Assuming you have a Profile model
            Profile.objects.create(user=user, firstname=firstname, lastname=lastname, phone=phone, gender=gender)

            messages.success(request, 'Registered Successfully!')
            return redirect('index')
        except Exception as e:
            messages.error(request, 'An error occurred during registration: {}'.format(e))
            return redirect('register')

    return render(request, 'register.html')





def logout_user(request):
    print("Logout function called.")  
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')






def submit_table_booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        people = request.POST.get('people')
        message = request.POST.get('message')

        # Save the data to the database
        booking = Custom_Table(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            people=people,
            message=message
        )
        booking.save()

        # Respond with a success message
        return HttpResponse("OK")  # Or redirect to another page

    # For GET requests, render the same or a different template
    return render(request, 'index.html')





from contact_report.models import Contact

from django.http import JsonResponse
def submit_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the data to the database
        contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()

        # Return a JSON response with the success message
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'message': "Invalid request."})