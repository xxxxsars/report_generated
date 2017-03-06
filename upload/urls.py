
from django.conf.urls import url,include
from .views import index,second_index,i,login,register,logout,redict

urlpatterns = [

    url(r"index/", i),
    url(r"^senior/", index, name="first"),
    url(r"^secondary/", second_index, name="second"),
    url(r'^login/',login),
    url(r"^register/",register,name="register"),
    url(r'^logout/',logout),
    url(r"",redict)


]