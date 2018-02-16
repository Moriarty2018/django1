from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^register/$',views.register,name='register'),
    url(r'^register_handler/$',views.register_handler,name='register_handler'),
    url(r'^login/$',views.login,name='login'),
    url(r'^login_handler/$',views.login_handler,name='login_handler'),
    url(r'^info/$',views.info,name='info'),
    url(r'^order_(\d+)/$',views.order,name='order'),
    url(r'^site/$',views.site,name='site'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^site_handle/$',views.site_handle,name='site_handle'),
]
