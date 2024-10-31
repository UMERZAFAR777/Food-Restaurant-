from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from info.models import Profile
from New_Menu.models import New_Menu,Section
from custom_birthday.models import Custom_Birthday
from chef.models import Chef










def index(request):
    menu = New_Menu.objects.all()
    section = Section.objects.prefetch_related('new_menu_set')
    birthday = Custom_Birthday.objects.all()
    chef = Chef.objects.all()


    data = {
        'menu':menu,
        'section':section,
        'birthday':birthday,
        'chef':chef,
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




def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Print statement for debugging (remove in production)
        print(f"Email: {email}, Password: {password}") 
        
        # Attempt to authenticate using email
        try:
            # Check if the user exists with the provided email
            user = User.objects.get(email=email)
            # If user exists, authenticate using username and password
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
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






