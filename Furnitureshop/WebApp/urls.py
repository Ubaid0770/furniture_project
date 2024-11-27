from django.urls import path
from WebApp import views

urlpatterns = [
    path('home/',views.homepage,name="home"),
    path('addwebproducts/',views.addwebproducts,name="addwebproducts"),
    path('webcontact/',views.webcontact,name="webcontact"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('productsfiltered/<cat_name>/',views.productsfiltered,name="productsfiltered"),
    path('singleproduct/<int:pro_id>/',views.singleproduct,name="singleproduct"),
    path('signup/',views.signup,name="signup"),
    path('',views.signin,name="signin"),
    path('saveuser/',views.saveuser,name="saveuser"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('savecart/',views.savecart,name="savecart"),
    path('cart/',views.cart,name="cart"),
    path('delete_Cart/<int:del_id>/',views.delete_Cart,name="delete_Cart"),
    path('path/',views.checkout,name="checkout"),
    path('savecheckout/',views.savecheckout,name="savecheckout"),
    path('payment/',views.payment,name="payment")
]