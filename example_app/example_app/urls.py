from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shop', views.ShopList.as_view()),
    url(r'^book', views.BookList.as_view()),
]
