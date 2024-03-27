from django.shortcuts import render,redirect
from blog.models import Blog_Category,Blog
from .models import product,Products_Category , Products_Category_Mega
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from comments.models import Comment_product
from django.db.models import Q,Count
from order_shop.models import Like_products
from django.contrib.auth.models import User
from django.http import JsonResponse
from order_shop.models import Order,OrderDetail
# Create your views here.


def Producst_List(request):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")

    #________________________ Order _________________________________________

    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    category_blog = Blog_Category.objects.all()
    prpducts = product.objects.order_by("-id").annotate(cmcm = Count("comments_counts"))
    if prpducts:
        last = int(product.objects.last().id) - 10
    else:
        last = 0
    paginator = Paginator(prpducts, 8)
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    context = {"category_blog":category_blog,"page_obj": page_obj,"products":prpducts,
               "last":last,"mega":category_product_mega,"category":category_product,"order_detail":order_detail,"order":order}

    if request.POST.get("number2"):
        price1 = request.POST.get("number2")[5:]
        price2 = request.POST.get("number")[5:]
        filter = request.POST.get("filter")
        price11 = price1.replace(",","")
        price22 = price2.replace(",","")
        print(filter)
        
        if filter == "4":
            prpductsw = product.objects.filter(price__gte=int(price11), price__lte=int(price22)).order_by("price").annotate(cmcm = Count("comments_counts"))
            context["page_obj"] = prpductsw
        elif filter == "5":
            prpductsw = product.objects.filter(price__gte=int(price11), price__lte=int(price22)).order_by("-price").annotate(cmcm = Count("comments_counts"))
            context["page_obj"] = prpductsw
        elif filter == "0":
            prpductsw = product.objects.filter(price__gte=int(price11), price__lte=int(price22)).annotate(cmcm = Count("comments_counts"))
            context["page_obj"] = prpductsw
        elif filter == "2":
            prpductsw = product.objects.filter(price__gte=int(price11), price__lte=int(price22), price_percent__isnull=False).annotate(cmcm = Count("comments_counts"))
            context["page_obj"] = prpductsw
        elif filter == "3":
            prpductsw = product.objects.filter(price__gte=int(price11), price__lte=int(price22)).order_by("-count_buy").annotate(cmcm = Count("comments_counts"))
            context["page_obj"] = prpductsw
        elif filter == "1":
            prpductsw = product.objects.filter(price__gte=int(price11), price__lte=int(price22)).order_by("-ranking_AVG").annotate(cmcm = Count("comments_counts"))
            context["page_obj"] = prpductsw

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

    return render(request,"product.html",context)




def modal_page(request):
    context = {}

    return render(request,"modal.html",context)



def category_product_page(request,pk):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")

    #________________________ Order _________________________________________

    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    category_blog = Blog_Category.objects.all()
    prpducts_one = product.objects.order_by("-id").annotate(cmcm = Count("comments_counts"))
    idx = Products_Category.objects.filter(enname = pk).first().id
    prpducts = product.objects.filter(category = idx).annotate(cmcm = Count("comments_counts"))
    paginator = Paginator(prpducts, 8)

    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    context = {"category_blog":category_blog,"mega":category_product_mega,
               "category":category_product,"page_obj": page_obj,"products":prpducts_one}

    if request.POST.get("number2"):
        price1 = request.POST.get("number2")[5:]
        price2 = request.POST.get("number")[5:]
        filter = request.POST.get("filter")
        price11 = price1.replace(",","")
        price22 = price2.replace(",","")
        print(filter)

        if filter == "4":
            prpducts = product.objects.filter(category = idx)
            product_cat = prpducts.filter(price__gte=int(price11), price__lte=int(price22)).order_by("price")
            
            context["page_obj"] = product_cat
        elif filter == "5":
            prpducts = product.objects.filter(category = idx)
            product_cat = prpducts.filter(price__gte=int(price11), price__lte=int(price22)).order_by("-price")
            context["page_obj"] = product_cat
        elif filter == "0":
            prpducts = product.objects.filter(category = idx)
            product_cat = prpducts.filter(price__gte=int(price11), price__lte=int(price22))
            context["page_obj"] = product_cat
            
        elif filter == "2":
            prpducts = product.objects.filter(category = idx)
            product_cat = prpducts.filter(price__gte=int(price11), price__lte=int(price22), price_percent__isnull=False)
            context["page_obj"] = product_cat

        elif filter == "3":
            prpducts = product.objects.filter(category = idx)
            product_cat = prpducts.filter(price__gte=int(price11), price__lte=int(price22)).order_by("-count_buy")
            context["page_obj"] = product_cat

        elif filter == "1":
            prpducts = product.objects.filter(category = idx)
            product_cat = prpducts.filter(price__gte=int(price11), price__lte=int(price22)).order_by("-ranking_AVG")
            context["page_obj"] = product_cat
            



    if request.POST.get("like"):
        idl = request.POST.get("like")
        producte = product.objects.get(id=idl)
        user = User.objects.get(id=request.user.id)
        like = Like_products.objects.create(product_like=producte, user_id=user)
        like.save()
    
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

    return render (request,"category_product.html",context)


def detail_product(request,pk):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")

    #________________________ Order _________________________________________
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    category_blog = Blog_Category.objects.all()
    info = product.objects.filter(id = pk).first() 

    
    if info is None:
        return redirect("/404")
    

    CMC = Comment_product.objects.filter(product_id = info).count()
    CMN = Comment_product.objects.filter(product_id=info).order_by('-id')
    prpducts_one = product.objects.order_by("-id").annotate(cmcm = Count("comments_counts"))
    print(CMC)
    context = {"info":info,"comments":CMN,"products":prpducts_one,"category_blog":category_blog,"mega":category_product_mega,"category":category_product,"order_detail":order_detail,"order":order}

    if request.POST.get("comment"):
        CMC_new = CMC + 1
        comment = request.POST.get("comment")
        name = request.POST.get("name")
        ranking = request.POST.get("ranking")
        chek = request.POST.get("chek")
        if chek == "true":
            CM = Comment_product.objects.create(comment = comment,name = "ناشناس",rank = ranking,product_id = info)
        else:
            CM = Comment_product.objects.create(comment = comment,name = name,rank = ranking,product_id = info)

            
        if info:
            info.ranking += int(ranking)
            info.ranking_AVG = info.ranking / CMC_new
            info.save()
            print(info.ranking_AVG)

    if request.POST.get("like"):
        idl = request.POST.get("like")
        producte = product.objects.get(id=idl)
        user = User.objects.get(id=request.user.id)
        like = Like_products.objects.create(product_like=producte, user_id=user)
        like.save()
        print("salllllllllllll")

    
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
        try:
            idl = request.POST.get("order_add")
            producte = product.objects.get(id=idl)
            count = request.POST.get("count_product")
            print(count)
            ordtl = OrderDetail.objects.filter(order = order,product = producte.id).first()
            product_update = product.objects.filter(id = idl).first()
            product_update.count_buy += 1
            product_update.save()

            if order is None:
                order = Order.objects.create(owner_id=request.user.id,is_pay=False)
                order.orderdetail_set.create(product_id=producte.id,count=int(count),price=producte.price)
            else:
                if ordtl:
                    ordtl.count += int(count) 
                    ordtl.save()
                elif ordtl is None:
                    order.orderdetail_set.create(product_id=producte.id,count=count,price=producte.price)
        except:
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

    return render(request,"product-details.html",context)







def serach_product(request):
    order = Order.objects.filter(owner_id=request.user.id,is_pay=False).first()
    order_detail = OrderDetail.objects.filter(order = order).order_by("-id")

    #________________________ Order _________________________________________
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    category_blog = Blog_Category.objects.all()
    context = {"category_blog":category_blog,"mega":category_product_mega,"category":category_product,"order_detail":order_detail,"order":order}

    if request.GET:
        data = request.GET.get("search")
        info = product.objects.filter(Q(title__contains= data) | Q(name__contains = data)).annotate(cmcm = Count("comments_counts"))
        context["page_obj"] = info

    if request.POST.get("like"):
        idl = request.POST.get("like")
        producte = product.objects.get(id=idl)
        user = User.objects.get(id=request.user.id)
        like = Like_products.objects.create(product_like=producte, user_id=user)
        like.save()

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

                
    

    return render(request,"search.html",context)







def not_find(request):
    category_product_mega = Products_Category_Mega.objects.all()
    category_product = Products_Category.objects.all()
    category_blog = Blog_Category.objects.all()
    context = {"category_blog":category_blog,"mega":category_product_mega,"category":category_product}

    return render(request,"page-not-found.html",context)