from django.urls import path
from .views import baseview,submitview,showproductview,deleteproductview,updateproductview,registerview,loginview,logoutview

urlpatterns = [
    path('base/',baseview,name='base'),
    path('submit/',submitview,name='submitform'),
    path('show/',showproductview,name='showall'),
    path('delete/<int:id>',deleteproductview,name='delete'),
    path('update/<int:id>',updateproductview,name='update'),
    path('register/',registerview,name='register'),
    path('login/',loginview,name='login'),
    path('logout/',logoutview,name='logout'),
]