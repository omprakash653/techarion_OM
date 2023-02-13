from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('getproducts/',views.getproducts,name='getproducts'),
    path('productdetail/',views.productdetail,name='productdetail'),
    path('createuser/',views.createuser,name='createuser'),
    # path('getuser/',views.getuser,name='getuser'),
    # path('createproducts/',views.createproducts,name='createproducts'),
    
]
