from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login, logout
from login_app.models import Person

# Create your views here.
def user_registration(request):
    request_method = request.method

    if request_method == "POST":

        user_name = request.POST["UserName"]
        password = request.POST["Password"]

        if len(user_name) > 0 and len(password) > 0:
            user = authenticate(request, username=user_name, password=password)
            print("users+",user)
            if user is None:
                user = get_user_model().objects.create_user(username=user_name, password=password)
                users = Person.objects.create(User_name=user_name, Password=password)
                user.save()

                if user is not None:
                    user.is_staff = True
                    user.save()
                context = {'message': 'Hi {}, you have Successfully registered your account !!!'.format(user_name)}
                return render(request, 'user_login.html', context)
            else:
                context = {'message': 'Hi {}, you have already hold an account !!!'.format(user_name)}
                return render(request, 'user_login.html', context)
    return render(request, 'user_registration.html')


def user_login(request):
    request_method = request.method
    if request_method == "POST":
        username = request.POST['UserName']
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)

            context = {"message": "Welcome {} !!!".format(username)}
            return resp
            return render(request, 'user_page.html', context)
        else:
            context = {"message": "{}, Try Again !!!".format(username)}
            return render(request, 'user_login.html', context)
    return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    context = {"message": "Successfully Logged out !!!"}
    return render(request, 'user_login.html', context)
