#coding=utf-8
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from hashlib import sha1
from .models import UserInfo
from django.http import HttpResponseRedirect,HttpResponse
from . import user_decorator
from my_goods.models import Goods
#from my_count.models import OrderDetailInfo,OrderInfo
from account.models import AccountDetailInfo,AccountInfo
from django.core.paginator import Paginator

def register(request):
    context = {'title':'天天生鲜注册'}
    return render(request,'user/register.html',context)

def register_handler(request):
    try:
        post = request.POST
        name = post.get('user_name')
        pwd = post.get('pwd')
        cpwd = post.get('cpwd')
        email = post.get('email')
        if pwd!=cpwd:
            return redirect(reverse('user:register'))
        s = sha1()
        s.update(pwd)
        pwd1 = s.hexdigest()
        user = UserInfo()
        user.uname = name
        user.uemail = email
        user.upwd = pwd1
        user.save()
        return redirect(reverse('user:login'))
    except Exception as e:
        print e
        return redirect(reverse('user:register'))
def login(request):
    context = {'title':'天天生鲜登录'}
    return render(request,'user/login.html',context)

def login_handler(request):
    try:
        post = request.POST
        name = post.get('username')
        pwd = post.get('pwd')
        jizhu = post.get('jizhu','0')
        users = UserInfo.objects.filter(uname=name)
        s = sha1()
        s.update(pwd)
        s1 = s.hexdigest()
        if s1==users[0].upwd:
            url = request.COOKIES.get('url', reverse('goods:index'))
            new_user = HttpResponseRedirect(url)

            if jizhu=='1':
                new_user.set_cookie('uname',name)
            request.session['u_id'] = users[0].id
            request.session['uname'] = name
            return new_user

        else:
            url = request.COOKIES.get('url', reverse('goods:index'))
            new_user = HttpResponseRedirect(url)
            return new_user

    except Exception as e:
        print e
        return redirect(reverse('user:login'))

@user_decorator.login
def info(request):
    name = request.session.get('uname',None)
    goods_ids = request.COOKIES.get('goods_ids','')
    goods_ids1 = goods_ids.split(',')
    list = []
    for x in goods_ids1:
        list.append(Goods.objects.get(pk=int(x)))
    context ={'title':'用户信息','name':name,'list':list}
    return render(request,'user/user_center_info.html',context)
@user_decorator.login
def order(request,tid):
    try:
        name = request.session.get('uname', None)
        user = UserInfo.objects.filter(uname=name)[0]
        ods = user.accountinfo_set.all()
        paginator = Paginator(ods, 2)
        print '以获取用户订单'
        all_num = paginator.num_pages
        page = paginator.page(tid)
        context = {'title': '用户订单','name':name,'ods':ods,'page':page,'paginator':paginator}
        return render(request, 'user/user_center_order.html', context)
    except Exception as e:
        print '异常为%s' % e
        return HttpResponse('访问订单页面不存在')
@user_decorator.login
def site(request):
    name = request.session.get('uname', None)
    user = UserInfo.objects.filter(uname=name)[0]
    context = {'title': '用户地址', 'user': user,'name':name}
    return render(request, 'user/user_center_site.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

@user_decorator.login
def site_handle(request):
    user_name = request.session.get('uname', None)
    user = UserInfo.objects.filter(uname=user_name)[0]
    post = request.POST
    name = post.get('sname')
    addres = post.get('saddres')
    tel = post.get('stel')
    user.ushouname = name
    user.uaddres = addres
    user.uphone = tel
    user.save()
    return redirect(reverse('user:site'))



