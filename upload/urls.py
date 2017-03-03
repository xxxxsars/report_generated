
from django.conf.urls import url,include
from .views import index,second_index,i

urlpatterns = [

    url(r"index/", i),
    url(r"^senior/", index, name="first"),
    url(r"^secondary/", second_index, name="second")

]