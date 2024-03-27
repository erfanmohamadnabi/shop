from django.shortcuts import render,redirect
from .models import Blog_Category,Blog
from users.models import Users
from comments.models import Comment_blog
from products.models import Products_Category , Products_Category_Mega
from order_shop.models import Order,OrderDetail

# Create your views here.

def blog_list(request):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")

    #________________________ Order _________________________________________
    category_blog = Blog_Category.objects.all()
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    data = Blog.objects.order_by("-id")
    # info = Blog.objects.filter()
    context = {"category_blog":category_blog,"info":data,"info_more":data,"mega":category_product_mega,"category":category_product,"order_detail":order_detail,"order":order}
    
    if request.POST.get("email_user"):
        email = request.POST.get("email_user")
        user = Users.objects.create(email_user = email)
        user.save()
    

    return render(request,"blog.html",context)

def blog_detail(request,pkb):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")

    #________________________ Order _________________________________________
    category_blog = Blog_Category.objects.all()
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    data = Blog.objects.order_by("-date_number")
    info = Blog.objects.filter(id = pkb).first() 
    Previous_nm = int(pkb) - 1
    next_nm = int(pkb) + 1
    Previous = Blog.objects.filter(id = Previous_nm).first() 
    next = Blog.objects.filter(id = next_nm).first() 
    CMN = Comment_blog.objects.filter(blog_id = info)

    if info is None:
        return redirect("/404")

    context = {"category_blog":category_blog,"info":info,"data":data,"Previous":Previous,"next":next,"CMN":CMN,"mega":category_product_mega,"category":category_product,"order_detail":order_detail,"order":order}

    if request.POST.get("email_user"):
        email = request.POST.get("email_user")
        user = Users.objects.create(email_user = email)
        user.save()

    if request.POST.get("message"):
        message = request.POST.get("message")
        CM = Comment_blog.objects.create(massage = message,blog_id = info)
        CM.save()

    return render(request,"blog-details.html",context)

def blog_category_page(request,pk):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")

    #________________________ Order _________________________________________
    category_blog = Blog_Category.objects.all()
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    data = Blog.objects.all()
    idx = Blog_Category.objects.filter(en_name = pk).first().id
    idxm = Blog_Category.objects.filter(en_name = pk).first()
    MG = Blog.objects.filter(category = idx)
    context = {"category_blog":category_blog,"mg":MG,"name":idxm,"mega":category_product_mega,"category":category_product,"order_detail":order_detail,"order":order}

    if request.POST.get("email_user"):
        email = request.POST.get("email_user")
        user = Users.objects.create(email_user = email)
        user.save()

    return render(request,"blog_category.html",context)
