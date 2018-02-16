from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.cart,name='cart'),
    url(r'^add(\d+)_(\d+)/$',views.add),
    url(r'^edit(\d+)_(\d+)/$',views.edit),
    url(r'^delete(\d+)/$',views.delete),
    url(r'^od_handle/$',views.od_handle,name='od_handle'),
    url(r'^new_od/$',views.new_od,name='new_od'),
    url(r'^buy_now/$',views.buy_now,name='buy_now'),
    url(r'^buy_now_handle/$',views.buy_now_handle,name='buy_now_handle'),
    url(r'^buy_order/$',views.buy_order,name='buy_order'),
]