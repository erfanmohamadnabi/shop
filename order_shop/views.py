from django.shortcuts import render,redirect
from .models import Like_products,Order,OrderDetail
from django.contrib.auth.models import User
from products.models import product
from django.contrib.auth.decorators import login_required
from blog.models import Blog_Category,Blog
from products.models import product,Products_Category , Products_Category_Mega
from django.http import HttpResponseRedirect
from order_shop.models import Order,OrderDetail
import zibal.zibal as zibal
from django.http import HttpResponseRedirect
# Create your views here.

@login_required(login_url="/login")
def Like_page(request):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")

    #________________________ Order _________________________________________
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    category_blog = Blog_Category.objects.all()
    user = User.objects.get(id=request.user.id)
    likes = Like_products.objects.filter(user_id=user).order_by('-id')
    context = {"likes":likes,"category_blog":category_blog,"mega":category_product_mega,"category":category_product,"order_detail":order_detail,"order":order}
    
    
    if request.POST.get("order_add"):
        print("saaaaaaaaaaa")
        idl = request.POST.get("order_add")
        producte = product.objects.get(id=idl)
        count = request.POST.get("count")
        ordtl = OrderDetail.objects.filter(order = order,product = producte.id).first()
        product_update = product.objects.filter(id = idl).first()
        product_update.count_buy += 1
        product_update.save()

        if order is None:
            order = Order.objects.create(owner_id=request.user.id,is_pay=False)
            if count:
                order.orderdetail_set.create(product_id=producte.id,count=int(count),price=producte.price)
            else:
                order.orderdetail_set.create(product_id=producte.id,count=1,price=producte.price)
        else:
            if ordtl:
                if count:
                    ordtl.count += int(count)
                else:
                    ordtl.count +=1
                ordtl.save()

            elif ordtl is None:
                if count:
                    order.orderdetail_set.create(product_id=producte.id,count=int(count),price=producte.price)
                else:
                    order.orderdetail_set.create(product_id=producte.id,count=1,price=producte.price)

    return render(request,"like.html",context)


@login_required(login_url="/login")
def Order_page(request):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    category_blog = Blog_Category.objects.all()
    user = User.objects.get(id=request.user.id)
    context = {"category_blog":category_blog,"mega":category_product_mega,"category":category_product,"order_detail":order_detail,"order":order}

    if request.POST.get("count"):
        count_products = request.POST.getlist("count")
        xid = request.POST.getlist("xid")
        for i, (count_product, xid) in enumerate(zip(count_products, xid)):
            order_update = OrderDetail.objects.filter(order = order , id = xid).first()
            order_update.count = count_product
            order_update.save()

    return render (request,"product-cart.html",context)


def delete_product_like(request,like_id):    
    if like_id is not None:
        order_detail =Like_products.objects.get(id = like_id)
        if order_detail is not None:
            order_detail.delete()
            return redirect("/Like_page")
    return redirect("/Like_page")



def delete_product_order_detail(request,order_detail_id):    
    if order_detail_id is not None:
        order_detail =OrderDetail.objects.get(id = order_detail_id)
        if order_detail is not None:
            order_detail.delete()
            return redirect("/Producst_List")
    return redirect("/Producst_List")


def delete_product_order_page(request,order_detail_id):    
    if order_detail_id is not None:
        order_detail =OrderDetail.objects.get(id = order_detail_id)
        if order_detail is not None:
            order_detail.delete()
            return redirect("/Order_page")
    return redirect("/Order_page")



@login_required(login_url="/login")
def final_payment(request):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")

    #________________________ Order _________________________________________


    merchant_id = '651c08dec3e07400172b16aa'
    callback_url = 'http://darvishi.shop/call'
    zb = zibal.zibal(merchant_id, callback_url)
    amount = 1000 * 10 # IRR

    #________________________ Payment _______________________________________
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    category_blog = Blog_Category.objects.all()
    context = {"category_blog":category_blog,"mega":category_product_mega,"category":category_product,"order_detail":order_detail,"order":order}

    if request.POST.get("fname"):
        name = request.POST.get("fname")
        lname = request.POST.get("lname")
        city = request.POST.get("city")
        addres = request.POST.get("addres")
        post_code = request.POST.get("post_code")
        phone = request.POST.get("phone")
        note = request.POST.get("note")
        checked = request.POST.get("payment")
        private = request.POST.get("private")
        
   
        if checked == "home":
            order.is_pay = True
            order.is_post = True
            order.save()

            order.fname = name
            order.lname = lname
            order.addres = city + " " + addres + f"کد پستی : {post_code}"
            order.phone = phone
            if note:
                order.note = note
            order.save()

        

            return redirect("/callback")

    return render(request,"product-checkout.html",context)


def callback(request):
    context = {}

    return render(request,"callback.html",context)