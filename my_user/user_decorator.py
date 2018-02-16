#coding=utf-8
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def login(func):
    def login_handle(request,*args,**kwargs):
        if request.session.has_key('u_id'):
            return func(request,*args,**kwargs)
        else:
            red = HttpResponseRedirect(reverse('user:login'))
            red.set_cookie('url',request.get_full_path())
            return red
    return login_handle