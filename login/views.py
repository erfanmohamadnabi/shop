from django.shortcuts import render,redirect
from .forms import SignIn,loginn
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.models import Blog_Category,Blog
from products.models import product,Products_Category , Products_Category_Mega
from django.http import JsonResponse
from users.models import Users
import random
from django.core.mail import send_mail


# Create your views here.

def signin_page(request):
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    category_blog = Blog_Category.objects.all()
    frm=SignIn(request.POST or None)
    frml=loginn(request.POST or None)
    context = {"frm":frm,"frml":frml,"category_blog":category_blog,"mega":category_product_mega,"category":category_product}
    code_request = request.POST.get("code_request")

    if request.POST:
        print("helolllll")
        if code_request == "sign_in":
            if frm.is_valid():
                data = frm.cleaned_data
                username = data.get("username")
                fname = data.get("fname")
                password = data.get("password")
                u = User.objects.create_user(username=username,password=password,first_name = fname)
                u.save()


                if username.isdigit() and len(username) == 11:
                    b = Users.objects.create(email_user = username)
                    b.save()

                if "@gmail.com" in username:
                    send_mail(
                     "به وستا خوش امدید !",
                    f" . برای اطلاع از تخفیفات عضو باشگاه مشتریان شوید",
                    "erfan.web8787@gmail.com",
                    [username]
                )
                    
                context["succes_sign"] = "با موفقیت ثبت نام شدید !!!"

        if code_request == "login":
            if frml.is_valid(): 
                username=frml.cleaned_data.get("username")
                password=frml.cleaned_data.get("password")
            
                U=authenticate(username=username,password=password)
                if U:
                    login(request,U)
                    return redirect("/Profile")
            
                context["login_error"]="نام کاربری یا رمز عبور اشتباه هست"

    return render(request,"account-login.html",context)


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")
    
    return redirect("/login")



def verify(request):
    context = {}

    if request.POST.get("email"):
        global number
        global user
        email = request.POST.get("email")
        user = User.objects.filter(username = email).first()
        number = random.randint(100000,900000)
        print(number)
        if user and "@gmail.com" in email:
            text_message = request.POST.get("message")
            send_mail(
            "کد تایید وستا",
            f"{number}",
            "erfan.web8787@gmail.com",
            [email]
        )
            
        else:
            response_data = {'message':"نام کاربری یافت نشد !!!"}
            return JsonResponse(response_data)

        

    if request.POST.get("verify_code"):
        code = request.POST.get("verify_code")
        print(code)
        print(number)
        if int(code) == number:
            # U=authenticate(username=user.username,password=user.password)
            login(request,user)
            return redirect("/Profile")

    return render(request,"verify.html",context)