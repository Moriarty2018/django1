#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from my_user import user_decorator
from models import *
from my_user.models import UserInfo
from my_goods.models import Goods
from decimal import *
from account.models import AccountInfo,AccountDetailInfo
from datetime import *
from django.db import transaction
from django.core.urlresolvers import reverse

@user_decorator.login
def cart(request):
    uid = request.session['u_id']
    name = request.COOKIES.get('uname')
    carts = CartInfo.objects.filter(user_id=uid)
    total_count = len(carts)
    context = {'title':'购物车','carts':carts,'name':name,'total_count':total_count}
    return render(request,'cart/cart.html',context)

@user_decorator.login
def add(request,gid,count):
    try:
        uid = request.session.get('u_id')
        gid = int(gid)
        count = int(count)
        carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)
        if len(carts)>=1:
            cart = carts[0]
            cart.count = cart.count + count
        else:
            cart = CartInfo()
            cart.user_id = uid
            cart.goods_id = gid
            cart.count = count
        cart.save()
        my_cart = CartInfo.objects.filter(user_id=request.session['u_id'])[0]
        my_count =my_cart.count

        return JsonResponse({'my_count':my_count})
    except Exception as e:
        print e
        return HttpResponse('l加入购物车失败')

@user_decorator.login
def edit(request,cart_id,count):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.count = int(count)
        count1 = cart.count
        cart.save()
        data = {'ok':0}
    except Exception as e:
        data = {'ok':count1}
    return JsonResponse(data)

@user_decorator.login
def delete(request,cart_id):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data = {'ok': 1}
    except Exception as e:
        data = {'ok': 0}
    return JsonResponse(data)

@transaction.atomic()
@user_decorator.login
def od_handle(request):
    trans_id = transaction.savepoint()
    #carts = request.POST.getlist('cart_id')
    try:
        new_account = AccountInfo()
        now = datetime.now()
        uid = request.session['u_id']
        new_account.acid = '%s%d'%(now.strftime('%Y%m%d%H%M%S'),uid)
        new_account.user_id = uid
        new_account.acdate = now
        new_account.actotle = Decimal(request.POST.get('total'))
        new_account.save()
        cart_list = request.POST.getlist('cart_id')
        print '已接受对方订单请求'
        for x in cart_list:
            detail = AccountDetailInfo()
            detail.account = new_account
            cart = CartInfo.objects.filter(pk=int(x))[0]
            goods = cart.goods
            if goods.gkucun>=cart.count:
                goods.gkucun = goods.gkucun - cart.count
                goods.save()
                detail.goods_id = goods.id
                detail.price = goods.gprice
                detail.count = cart.count
                detail.save()
                print '货号为%d的商品已保存' % goods.id
            else:
                transaction.savepoint_rollback(trans_id)
                return redirect('/my_cart/')
        return redirect('/user/order_1/')
    except Exception as e:
        print '异常为%s' % e
        transaction.savepoint_rollback(trans_id)
        return HttpResponse('异常为%s' % e)

@user_decorator.login
def buy_now_handle(request):
    try:
        request.session['g_id'] = request.POST.get('g_id')
        request.session['gnum'] = request.POST.get('num')
        data = {'ok':1}
        return JsonResponse(data)
    except Exception as e:
        print e
        data = {'ok':0}
        return JsonResponse(data)

@user_decorator.login
def buy_now(request):
    name = request.session.get('uname')
    new_user = UserInfo.objects.filter(uname=name)[0]
    mid = request.session.get('g_id')
    count = request.session.get('gnum')
    count = int(count)
    my_goods = Goods.objects.filter(pk=int(mid))[0]
    title = '提交订单'
    context = {'title': title, 'my_goods': my_goods, 'new_user': new_user,'count':count,'name':name}
    return render(request, 'mcount/buy_order.html', context)

@transaction.atomic()
@user_decorator.login
def buy_order(request):
    trans_id = transaction.savepoint()
    try:
        count = request.GET['num']
        gid = request.GET['gid']
        gid = int(gid)
        shuliang = int(count)
        new_account = AccountInfo()
        now = datetime.now()
        uid = request.session['u_id']
        new_account.acid = '%s%d'%(now.strftime('%Y%m%d%H%M%S'), uid)
        new_account.user_id = uid
        new_account.acdate = now
        new_account.actotle = Decimal(str(request.GET['total']))
        new_account.save()
        detail = AccountDetailInfo()
        detail.account = new_account
        new_goods = Goods.objects.filter(pk=gid)[0]
        print '已经接受请求'
        if new_goods.gkucun >= shuliang:
            new_goods.gkucun = new_goods.gkucun - shuliang
            new_goods.save()
            detail.goods = new_goods
            detail.price = new_goods.gprice
            detail.count = shuliang
            detail.save()
            return JsonResponse({'ok': 1})
        else:
            transaction.savepoint_rollback(trans_id)
            return JsonResponse({'ok': 2})

    except Exception as e:
        print e
        transaction.savepoint_rollback(trans_id)
        return JsonResponse({'ok': 0})

@user_decorator.login
def new_od(request):
    name = request.COOKIES.get('uname')
    new_user = UserInfo.objects.filter(uname=name)[0]
    my_list = request.POST.getlist('cart_id')
    cart_list = []
    for x in my_list:
        new_cart = CartInfo.objects.filter(pk=int(x))[0]
        cart_list.append(new_cart)
    title = '提交订单'
    context ={'title':title,'cart_list':cart_list,'new_user':new_user}
    return render(request,'mcount/place_order.html',context)

