#coding=utf-8
from django.shortcuts import render,redirect
from .models import TypeInfo,Goods
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.http import HttpResponse


def index(request):
    name = request.session.get('uname','')
    type_list = TypeInfo.objects.all()
    type0 = type_list[0].goods_set.order_by('-id')[0:4]
    type01 = type_list[0].goods_set.order_by('-gclick')[0:4]
    type1 = type_list[1].goods_set.order_by('-id')[0:4]
    type11 = type_list[1].goods_set.order_by('-gclick')[0:4]
    type2 = type_list[2].goods_set.order_by('-id')[0:4]
    type21 = type_list[2].goods_set.order_by('-gclick')[0:4]
    type3 = type_list[3].goods_set.order_by('-id')[0:4]
    type31 = type_list[3].goods_set.order_by('-gclick')[0:4]
    type4 = type_list[4].goods_set.order_by('-id')[0:4]
    type41 = type_list[4].goods_set.order_by('-gclick')[0:4]
    type5 = type_list[5].goods_set.order_by('-id')[0:4]
    type51 = type_list[5].goods_set.order_by('-gclick')[0:4]
    context = {'title':'首页','type0':type0,'type01':type01,'type1':type1,
               'type11':type11,'type2':type2,'type21':type21,
               'type3':type3,'type31':type31,'type4':type4,
               'type41':type41,'type5':type5,'type51':type51,'name':name,
               }
    return render(request,'goods/index.html',context)

def list(request,tid,pindex,sort):
    try:
        name = request.session.get('uname', '')
        new_id = int(tid)
        typeinfo = TypeInfo.objects.get(pk=int(tid))
        news = typeinfo.goods_set.order_by('-id')[0:2]
        if sort=='1':
            goods_list = Goods.objects.filter(gtype_id=int(tid)).order_by('-id')
        elif sort=='2':
            goods_list = Goods.objects.filter(gtype_id=int(tid)).order_by('-gprice')
        elif sort=='3':
            goods_list = Goods.objects.filter(gtype_id=int(tid)).order_by('-gclick')
        else:
            goods_list = Goods.objects.filter(gtype_id=int(tid)).order_by('-id')
        paginator = Paginator(goods_list,10)
        page = paginator.page(int(pindex))
        context = {
            'title':typeinfo.title,'page':page,
            'paginator':paginator,'news':news,
            'typeinfo':typeinfo,'sort':sort,'name':name,'new_id':new_id,
        }
        return render(request,'goods/list.html',context)
    except Exception as e:
        print e
        return HttpResponse('请求页面不存在')
def detail(request,id):
    name = request.session.get('uname', '')
    try:
        my_good = Goods.objects.get(pk=int(id))
        my_good.gclick = my_good.gclick +1
        my_good.save()
        news = my_good.gtype.goods_set.order_by('-id')[0:2]
        context = {
            'title':my_good.gtype.title,'goods':my_good,
            'id':id,'news':news,'name':name,
        }
        response = render(request,'goods/detail.html',context)
        goods_ids = request.COOKIES.get('goods_ids','')
        #goods最近浏览
        goods_id = '%d'%my_good.id
        if goods_ids != '':
            goods_ids1 = goods_ids.split(',')
            if goods_ids1.count(goods_id)>=1:
                goods_ids1.remove(goods_id)
            goods_ids1.insert(0,goods_id)
            if len(goods_ids1)>=6:
                goods_ids1[0:5]
            goods_ids = ','.join(goods_ids1)
        else:
            goods_ids = goods_id
        response.set_cookie('goods_ids',goods_ids)
        return response
    except Exception as e:
        print e
        return HttpResponse('请求商品不存在')
