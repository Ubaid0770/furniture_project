from django.urls import path
from FurnitureApp import views

urlpatterns = [
   path('index/',views.index,name="index"),
   path('addcategoryfn/',views.addcategoryfn,name="addcategoryfn"),
   path('savecategoryfn/',views.savecategoryfn,name="savecategoryfn"),
   path('displaycategoryfn/',views.displaycategoryfn,name="displaycategoryfn"),
   path('editcategoryfn/<int:edit_id>/',views.editcategoryfn,name="editcategoryfn"),
   path('updatecategoryfn/<int:edit_id>/',views.updatecategoryfn,name="updatecategoryfn"),
   path('deletecategoryfn/<int:del_id>',views.deletecategoryfn,name="deletecategoryfn"),
   path('addproductfn/',views.addproductfn,name="addproductfn"),
   path('saveproductfn/',views.saveproductfn,name="saveproductfn"),
   path('displayproductfn/',views.displayproductfn,name="displayproductfn"),
   path('editproductfn/<int:editprod_id>/',views.editproductfn,name="editproductfn"),
   path('update/<int:editprod_id>/',views.updateproductfn,name="update"),
   path('delete/<int:dell_id>/',views.deleteproductfn,name="delete"),
   path('adminpage/',views.adminpage,name="adminpage"),
   path('adminlogin/',views.adminlogin,name="adminlogin"),
   path('adminlogout/',views.adminlogout,name="adminlogout"),
   path('displaycontact/',views.displaycontact,name="displaycontact")
]
