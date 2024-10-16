from django.contrib import admin
from django.urls import path,include
from user import views
from .views import GeneratePdf
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('Home', views.Home, name='Home'),
    #-----------------------------------------------------------------------
    path('pdf/',GeneratePdf.as_view(),name='pdf'),
    #-----------------------------------------------------------------------
    path('Supplier_Register', views.Supplier_Register, name='Supplier_Register'),
    path('Suppliers_Store', views.Suppliers_Store, name='Suppliers_Store'),
    #-----------------------------------------------------------------------
    path('Suppliers_login', views.Suppliers_login, name='Suppliers_login'),
    path('Suppliers_Check', views.Suppliers_Check, name='Suppliers_Check'),
    path('supplier_forget', views.supplier_forget, name='supplier_forget'),
    path('supplier_forget_chk', views.supplier_forget_chk, name='supplier_forget_chk'),
    path('changePassword', views.changePassword, name='changePassword'),    
    path('supplier_change_pass', views.supplier_change_pass, name='supplier_change_pass'),
    #-----------------------------------------------------------------------
    path('load_areas/', views.load_areas, name='load_areas'),
    #-----------------------------------------------------------------------
    path('clear_message/', views.clear_message, name='clear_message'),
    #-----------------------------------------------------------------------
    path('User_Register', views.User_Register, name='User_Register'),
    path('User_Store', views.User_Store, name='User_Store'),
    #-----------------------------------------------------------------------
    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('user_forget', views.user_forget, name='user_forget'),
    path('user_forget_chk', views.user_forget_chk, name='user_forget_chk'),
    path('user_change_pass', views.user_change_pass, name='user_change_pass'),
    #-----------------------------------------------------------------------
    path('about', views.about, name='about'),
    #-----------------------------------------------------------------------
    path('shop', views.shop, name='shop'),
    #-----------------------------------------------------------------------
    path('feedback', views.feedback, name='feedback'),
    path('feedback_store', views.feedback_store, name='feedback_store'), 
    #-----------------------------------------------------------------------
    path('inquiry', views.inquiry, name='inquiry'), 
    path('inquiry_store', views.inquiry_store, name='inquiry_store'),
    #-----------------------------------------------------------------------
    path('viewmore/<int:id>', views.viewmore, name='viewmore'),
    #-----------------------------------------------------------------------
    path('order_page/<int:id>', views.order_page, name='order_page'),
    path('order_store/<int:id>', views.order_store, name='order_store'),
    #-----------------------------------------------------------------------
    path('Payment/<int:id>', views.Payment, name='Payment'),
    path('success', views.success, name='success'),
    #-----------------------------------------------------------------------
    path('user_profile', views.user_profile, name='user_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    #-----------------------------------------------------------------------
    path('view_my_order', views.view_my_order, name='view_my_order'),
    path('track_order/<int:id>', views.track_order, name='track_order'),
    path('test',views.test,name="test"),
    # path('single_product',views.single_product,name="single_product"),
    path('single_product/<int:id>', views.single_product, name='single_product'),
    
    
    #-----------------------------------------------------------------------
    path('receipt_viewmore/<int:id>',views.receipt_viewmore,name="receipt_viewmore"),
    
    path('category',views.category, name='category'),

    #-----------------------------------------------------------------------
    path('logout', views.logout, name='logout'),
    
    
    
    
    path('viewProduct/<int:id>',views.viewProduct,name="viewProduct"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)