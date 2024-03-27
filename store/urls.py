from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from login.views import signin_page,logout_page,verify
from blog.views import blog_list,blog_detail,blog_category_page
from aboutus.views import AboutUs_page,Faq
from contact.views import ContactUs_Page
from products.views import Producst_List,category_product_page,detail_product,serach_product,not_find,modal_page
from order_shop.views import Like_page,delete_product_like,delete_product_order_detail,Order_page,delete_product_order_page,final_payment,callback
from userprofile.views import Profile
from index.views import Home,law

urlpatterns = [
    # path('', include('admin_soft.urls')),
    path('admin/', admin.site.urls),
    path('login', signin_page),
    path('verify', verify),
    path('', Home),
    path('law', law),
    path('aboutUs', AboutUs_page),
    path('faq', Faq),
    path('contact', ContactUs_Page),
    path('log_out', logout_page),
    path('blog_list', blog_list),
    path('Profile', Profile),
    path('Producst_List', Producst_List),
    path('serach_product', serach_product),
    path('404', not_find),
    path('modal_page', modal_page),


    path('category_product/<pk>', category_product_page,name="category_product_page"),
    path('blog-details/<pkb>', blog_detail,name="blog-details"),
    path('callback', callback,name="callback"),
    path('Like_page', Like_page,name="Like_page"),
    path('final_payment', final_payment,name="final_payment"),
    path('Order_page', Order_page,name="Order_page"),
    path('blog_category_page/<pk>', blog_category_page,name="Category_blog_page"),
    path('detail_product/<pk>', detail_product,name="detail_product"),



    path('delete_product_like/<like_id>',delete_product_like),
    path('delete_product_order_detail/<order_detail_id>',delete_product_order_detail),
    path('delete_product_order_page/<order_detail_id>',delete_product_order_page),

]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

