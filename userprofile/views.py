from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.models import Blog_Category,Blog
from products.models import product,Products_Category , Products_Category_Mega
from order_shop.models import Order,OrderDetail
# Create your views here.

@login_required(login_url="/login")
def Profile(request):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")
    history = Order.objects.filter(owner_id=request.user.id,is_pay=True).order_by("-id")

    #________________________ Order _________________________________________
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    category_blog = Blog_Category.objects.all()
    context = {"category_blog":category_blog,"mega":category_product_mega,"category":category_product,"order_detail":order_detail,"order":order,"history":history}
    user = User.objects.filter(username = request.user.username).first()

    if request.POST:
        password = request.POST.get("password")
        password_again = request.POST.get("password2")
        user = User.objects.filter(username = request.user.username).first()
        if password == password_again and len(password) >= 8:
            user.set_password(password)
            user.save()

            context["succes"] = "رمز عبور با موفقیت تغییر کرد"
        else:
            context["no_change"] = "رمز های عبور برابر نیستند !!!"
        

    return render(request,"my-account.html",context)