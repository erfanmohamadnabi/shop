from django.shortcuts import render
from products.models import Products_Category , Products_Category_Mega,product
from order_shop.models import Order,OrderDetail
from blog.models import Blog_Category,Blog
from django.db.models import Q,Count
from order_shop.models import Like_products
from django.contrib.auth.models import User
from comments.models import Comment_product
from django.http import JsonResponse
from users.models import Users

# Create your views here.


def Home(request):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")

    #________________________ Order _________________________________________

    prpducts = product.objects.order_by("-id").annotate(cmcm = Count("comments_counts"))
    prpductso = product.objects.filter(buy = True).annotate(cmcm = Count("comments_counts"))
    products_buy = product.objects.order_by("-count_buy").annotate(cmcm = Count("comments_counts"))

    #________________________ Products ______________________________________
    category_blog = Blog_Category.objects.all()
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    data = Blog.objects.order_by("-id")
    context = {"category_blog":category_blog,"mega":category_product_mega,
               "category":category_product,"order_detail":order_detail,"order":order,"page_obj":prpducts,"info":data,"products_buy":products_buy,"prpductso":prpductso}
    

    if request.POST.get("email_user"):
        email = request.POST.get("email_user")
        user = Users.objects.create(email_user = email)
        user.save()
    
    if request.POST.get("like"):
        idl = request.POST.get("like")
        producte = product.objects.get(id=idl)
        user = User.objects.get(id=request.user.id)
        like = Like_products.objects.create(product_like=producte, user_id=user)
        like.save()
        print("salam")


    if request.POST.get("fast_visit"):
        print("salam")
        idl = request.POST.get("fast_visit")
        comment_count = Comment_product.objects.filter(product_id = idl).count()
        visit = product.objects.filter(id = idl).first()
        username = request.user.id
        context["visit_product"] = visit
        if visit.buy == True:
            response_data = {'message': str(visit.category),"product_name":str(visit.name),"price_product":"فروش عمده" ,
                         "text_product":visit.text ,"comment_count":f"{comment_count} دیدگاه",
                         "img_link":visit.image.url,"stars":visit.ranking_AVG,"id_pruduct":visit.id,"user_ahetnticate":username}
        else:
            response_data = {'message': str(visit.category),"product_name":str(visit.name),"price_product":str(visit.price) + " تومان" ,
                         "text_product":visit.text ,"comment_count":f"{comment_count} دیدگاه",
                         "img_link":visit.image.url,"stars":visit.ranking_AVG,"id_pruduct":visit.id,"user_ahetnticate":username}
            
        return JsonResponse(response_data)


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

    return render(request,"index.html",context)


def law(request):
    context = {}

    return render(request,"law.html",context)