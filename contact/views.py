from django.shortcuts import render
from blog.models import Blog_Category,Blog
from .models import Message
from products.models import Products_Category , Products_Category_Mega
from order_shop.models import Order,OrderDetail
# Create your views here.

def ContactUs_Page(request):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")

    #________________________ Order _________________________________________
    category_blog = Blog_Category.objects.all()
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    context = {"category_blog":category_blog,"mega":category_product_mega,"category":category_product,"order_detail":order_detail,"order":order}

    if request.POST:
        name = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        ME = Message.objects.create(name = name,last_name = lname,email = email,message = message)
        ME.save()

    return render(request,"contact.html",context)