from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils.translation.trans_real import catalog
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import *
from .forms import *
import datetime
import random
import telebot

# Create your views here.

def index(request):
    items = Tovar.objects.all()
    size = Size.objects.all()
    cat = Category.objects.all()
    carts = Cart.objects.all()
    c = 0
    for one in carts:
        c += one.count
    randTov =[]
    for i in range(0,6):
        randTov.append(random.choice(items))
    data = {'items': items, 'size': size, 'cat': cat, 'randTov': randTov,'carts':carts,'c':c}
    return render(request, 'index.html', data)


def forman(request):
    items = Tovar.objects.filter(group__id=1)
    itemslen = len(items)
    size = Size.objects.all()
    cat = Category.objects.all()
    carts = Cart.objects.all()
    c = 0
    for one in carts:
        c += one.count
    data = {'items': items, 'cat': cat, 'group': 1, 'size': size,'itemslen': itemslen,'c':c,'carts':carts}
    return render(request, 'catalog.html', data)

def formancat(request, cat2):
    items = Tovar.objects.filter(group__id=1)
    cat = Category.objects.all()
    size = Size.objects.all()
    items = Tovar.objects.filter(group__id=1, category__name=cat2)
    itemslen = len(items)
    carts = Cart.objects.all()
    c = 0
    for one in carts:
        c += one.count
    data = {'items': items, 'cat': cat, 'cat2': cat2,'group': 1, 'size': size,'itemslen': itemslen,'c':c,'carts':carts}
    return render(request, 'catalog.html', data)

def forwoman(request):
    items = Tovar.objects.filter(group__id=2)
    itemslen = len(items)
    cat = Category.objects.all()
    size = Size.objects.all()
    carts = Cart.objects.all()
    c = 0
    for one in carts:
        c += one.count
    data = {'items': items, 'cat': cat, 'group': 2, 'size': size,'itemslen': itemslen,'c':c,'carts':carts}
    return render(request, 'catalog.html',data)

def forwomancat(request, cat2):
    items = Tovar.objects.filter(group__id=2)
    cat = Category.objects.all()
    size = Size.objects.all()
    items = Tovar.objects.filter(group__id=2, category__name=cat2)
    itemslen = len(items)
    carts = Cart.objects.all()
    c = 0
    for one in carts:
        c += one.count
    data = {'items': items, 'cat': cat, 'cat2': cat2,'group': 2, 'size': size,'itemslen': itemslen,'c':c,'carts':carts}
    return render(request, 'catalog.html', data)

def otovare(request, itemid):
    items = Tovar.objects.filter(name=itemid)
    size = Size.objects.all()
    carts = Cart.objects.all()
    c = 0
    for one in carts:
        c += one.count
    data = {'items': items, 'size': size,'c':c,'carts':carts}
    return render(request,'otovare.html',data)


def cabinet(request):
    orders = Order.objects.filter(user_id=request.user.id)
    likes = like.objects.filter(user_id=request.user.id)
    carts = Cart.objects.all()
    c = 0
    for one in carts:
        c += one.count
    data = {'orders':orders,'c':c,'carts':carts,'likes':likes}
    return render(request,'cabinet.html', data)

def registration(request):
    if request.POST:
        print(1)
        form = UserForm(request.POST)
        if form.is_valid():
            print(2)
            k1= form.cleaned_data['username']
            k2= form.cleaned_data['email']
            k3=form.cleaned_data['password1']
            k4=form.cleaned_data['first_name']
            k5=form.cleaned_data['last_name']
            User.objects.create_user(username=k1,email=k2,password=k3)
            myuser = User.objects.get(username=k1)
            myuser.first_name = k4
            myuser.last_name = k5
            myuser.save()#сохраняем таблицу
            login(request,myuser) #автовход на сайт
            return redirect('cabinet')
    else:
        form = UserForm()

    data = {'form': form}
    return render(request,'registration/reg.html', data)


def cart(request):
    items = Cart.objects.filter(user_id=request.user.id)
    itemslen = len(items)
    carts = Cart.objects.all()
    c = 0
    for one in carts:
        c += one.count
    total = 0
    sps = ''
    form = OrderForm()
    for one in items:
        total += one.summa

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            k1 = form.cleaned_data['adres']
            k2 = form.cleaned_data['telephone']
            zakaz = ''
            for one in items:
                zakaz += one.tovar.name + ' ' + str(one.count) + 'шт ' + str(one.summa) + 'руб<br>'
            zakaz += "Всего: " + str(total) + 'руб<br>'
            zakaz += "Адрес: " + k1 + '<br>'
            zakaz += "Телефон: " + k2 + '<br>'
            zakaz += "Пользователь: " + request.user.username + '<br>'
            status = Status.objects.get(id=1)
            Order.objects.create(adress=k1, tel=k2, user_id=request.user.id,
                                 total=total, status=status,
                                 zakaz=zakaz, email=request.user.email,
                                 data=datetime.datetime.now())

            items.delete()
            total = 0
            sps = 'Спасибо за заказ ' + request.user.username
            telegram('Заказ :')
            zakaznew = zakaz.replace('<br>', '\n')
            telegram(zakaznew)

    data = {'items': items, 'total': total, 'form': form,'itemslen': itemslen,'sps':sps,'c':c,'carts':carts}
    return render(request, 'cart.html', data)

def edit(request, itemid,num):
    item = Cart.objects.get(id=itemid)
    num = int(num)
    item.count += num
    item.summa = item.calcSumma()
    if item.count > 0:
        item.save()
        return redirect('cart')
    else:
        return redirect('delete', itemid)

def delete(request, itemid):
    item = Cart.objects.get(id=itemid)
    item.delete()
    return redirect('cart')

def buy(request,itemid):
    item = Tovar.objects.get(id=itemid)
    user = request.user.id
    if Cart.objects.filter(user_id=user,tovar_id=item):
        item = Cart.objects.get(user_id=user,tovar_id=item.id)
        item.count +=1
        item.summa = item.calcSumma()
        item.save()
    else:
        Cart.objects.create(user_id=user,tovar_id=item.id,count=1,
                            summa=item.price)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def telegram(message):
    adres = 't.me/Boriscatalog2_bot'
    token = '8042919855:AAHt80S0GU-0U4pdAv9y3TdcBtr8LxxUgUk'
    chat = '279315648'
    bot = telebot.TeleBot(token)
    bot.send_message(chat, message)

def tolike(request):
    if request.GET:
        k1 = request.GET.get('k1')
        k2 = request.GET.get('k2')
        print(k1,k2)
        if like.objects.filter(user_id=request.user.id, tovar_id=k1):
            item = like.objects.get(user_id=request.user.id, tovar_id=k1)
            item.delete()
        else:
            like.objects.create(user_id=request.user.id,tovar_id=k1)
        return JsonResponse({'message':'успешно'})
