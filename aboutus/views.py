from django.shortcuts import render
from blog.models import Blog_Category
from products.models import Products_Category , Products_Category_Mega
# Create your views here.
from order_shop.models import Order,OrderDetail

def AboutUs_page(request):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")

    #________________________ Order _________________________________________
    category_blog = Blog_Category.objects.all()
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    context = {"category_blog":category_blog,"mega":category_product_mega,"category":category_product,"order_detail":order_detail,"order":order}
    return render(request,"about-us.html",context)

def Faq(request):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")

    #________________________ Order _________________________________________
    category_blog = Blog_Category.objects.all()
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    context = {"category_blog":category_blog,"mega":category_product_mega,"category":category_product,"order_detail":order_detail,"order":order}

    return render(request,"faq.html",context)
