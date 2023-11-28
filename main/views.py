import datetime
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from main.forms import ItemForm
from main.models import Item
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    data_count = items.count()

    context = {
        'application_name': 'RAF Inventory',
        'name': request.user.username,
        'class': 'PBP KKI',
        'items': items,
        'data_count': data_count,
        'last_login': request.COOKIES['last_login']
        if 'last_login' in request.COOKIES.keys()
        else "",
    }

    return render(request, 'main.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def delete(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return redirect('main:show_main')

def increment(request, id):
    item = Item.objects.get(pk=id)
    item.amount += 1
    item.save()
    return redirect('main:show_main')

def decrement(request, id):
    item = Item.objects.get(pk=id)
    if item.amount > 0:
        item.amount += -1
        item.save()
    else:
        item.amount = 0
    return redirect('main:show_main')

def edit(request, id):
    item = Item.objects.get(pk = id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "edit_item.html", context)

def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        category = request.POST.get("category")
        power = request.POST.get("power")
        rating = request.POST.get("rating")
        user = request.user

        new_product = Item(name=name, amount=amount, description=description, category=category, power=power, user=user, rating=rating)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            description = data["description"],
            category = data["category"],
            power = int(data["power"])
            )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)