from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.contrib import messages
from .form import ImageForm, GalleryImageForm
from random import seed
from random import randint
from django.http import JsonResponse
import json
import datetime 

@api_view(['GET'])
def login(request):
    request.session['loginID'] = "Nothing"
    logged = request.session['loginID']

    context = {
        "logged" : logged
    }

    data = {
        "response": "Success"
    }

    return Response(data)

def loginuser(request):
    errors = User.objects.logValidator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/')
    
    if request.POST['password'] == "adminPassword":
        request.session['loginID'] = "admin"
    else:
        new_user = User.objects.create(password=request.POST['password'])
        request.session['loginID'] = new_user.id
    return redirect('/index')

def index(request):
    print("**********************")
    print("**********************")
    print("**********************")
    print("***** IN INDEX FUNCTION *****")

    allItems = Items.objects.all()
    allImages = Image.objects.all()

    print("items below: ")
    print(allItems)
    for item in allItems:
        print(item)
        print(item.imgNums)

    print(allImages)
    for img in allImages:
        print(img)
        print(img.image)

    logged = request.session['loginID']
    admin = "admin"

    if logged == "Nothing":
        return redirect('/')

    print("logged here")
    print(logged)
    print("admin here")
    print(admin)

    context = {
        "allItems" : allItems,
        "allImages" : allImages,
        "logged" : logged,
        "admin" : admin
    }

    return render(request, "pages/index.html", context)

def addItem(request):
    logged = request.session['loginID']

    if logged != "admin":
        return redirect('/')

    if request.method == "POST":
        print("it is a post request")
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            print("the form is valid")
            form.save()
            obj=form.instance
            
            newItem = Items.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                price=request.POST['price'],
                imgNums = [obj.id]
            )
            newItem.save()
        
        return redirect('/index')
    else:
        form=ImageForm() 
        logged = request.session['loginID']

        context = {
            "form" : form,
            "logged" : logged
        }
    return render(request, "addItem.html", context)

def itemInfo(request, id):

    item = Items.objects.get(id=id)

    imgNumslen = len(item.imgNums)

    imgNumArr = item.imgNums

    admin = "admin"

    allPics = Image.objects.all()

    logged = request.session['loginID']

    if logged == "Nothing":
        return redirect('/')

    context = {
        "item" : item,
        "allPics" : allPics,
        "imgNumslen" : imgNumslen,
        "imgNumArr" : imgNumArr,
        "logged" : logged,
        "admin" : admin
    }

    return render(request, "pages/itemInfo.html", context)

def editItem(request, id):
    logged = request.session['loginID']

    if logged != "admin":
        return redirect('/')

    if request.method == "POST":
        print("it is a post request")
        item = Items.objects.get(id=id)
        allImages = Image.objects.all()
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            print("the form is valid")
            form.save()
            obj=form.instance
            
            item.imgNums += [obj.id]
            item.save()
        
        return redirect('/index')
    else:
        form=ImageForm() 
        item = Items.objects.get(id=id)
        allImages = Image.objects.all()

        numArr = item.imgNums
        indexArr = []
        ind = 1

        for i in numArr:
            if i != None:
                indexArr.append(ind)
                ind += 1

        indLen = len(indexArr)


        arrLen = indLen // 2
        lenArr = []

        print("new list here: ")
        print(item.imgNums)

        for i in range(2):
            lenArr.append(i)
        
        logged = request.session['loginID']

        context = {
            "form" : form,
            "item" : item,
            "allImages" : allImages,
            "indexArr" : indexArr,
            "lenArr" : lenArr,
            "logged" : logged
        }

    return render(request, "editItem.html", context)

def addImage(request, id):
    logged = request.session['loginID']

    if logged != "admin":
        return redirect('/')

    if request.method == "POST":
        print("it is a post request")
        item = Items.objects.get(id=id)
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            print("the form is valid")
            form.save()
            obj=form.instance
            
            item.imgNums += obj.id
            item.save()
        return redirect('/editItem/${id}')


def gallery(request):

    print("Session here:*********")
    print(request.session['loginID'])

    logged = request.session['loginID']

    if logged == "Nothing":
        return redirect('/')

    gIMD = []
    gImages = []

    _gIMD = GalleryImageDesc.objects.all()

    for imgd in reversed(_gIMD):
        gIMD.append(imgd)

    print("UNDERSCORE GIMD BELOW")
    print(_gIMD)
    print("GIMD BELOW")
    print(gIMD)

    _gImages = GalleryImage.objects.all()

    for img in reversed(_gImages):
        gImages.append(img)

    print("UNDERSCORE GIMAGES BELOW")
    print(_gImages)
    print("GIMAGES BELOW")
    print(gImages)

    context = {
        "gImages" : gImages,
        "gIMD" : gIMD,
        "logged" : logged
    }

    return render(request, "pages/gallery.html", context)

def galleryView(request, id):

    image = GalleryImageDesc.objects.get(id=id)

    print("description here: ")
    print(image.description)
    print("Id here: ")
    print(image.id)

    allGImages = GalleryImage.objects.all()

    prevImg = image.id - 1
    nextImg = image.id + 1
    logged = request.session['loginID']

    if logged == "Nothing":
        return redirect('/')

    context = {
        "image" : image,
        "prevImg" : prevImg,
        "nextImg" : nextImg,
        "allGImages" : allGImages,
        "logged" : logged
    }

    return render(request, "pages/galleryView.html", context)

def addGallery(request):
    logged = request.session['loginID']

    if logged != "admin":
        return redirect('/')

    if request.method == "POST":
        print("it is a post request")
        form=GalleryImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            print("the form is valid")
            form.save()
            obj=form.instance

            gImage = GalleryImageDesc.objects.create(description=request.POST['description'], image=obj.id)
            
        return redirect('/gallery')
    form = GalleryImageForm()
    logged = request.session['loginID']

    context = {
        "form" : form,
        "logged" : logged
    }

    return render(request, "addGallery.html", context)


def contact(request):
    print("Session here:*********")
    print(request.session['loginID'])
    logged = request.session['loginID']

    if logged == "Nothing":
        return redirect('/')

    context = {
        "logged" : logged
    }
    return render(request, "pages/contact.html", context)

def FAQ(request):
    print("Session here:*********")
    print(request.session['loginID'])
    logged = request.session['loginID']

    if logged == "Nothing":
        return redirect('/')

    context = {
        "logged" : logged
    }
    return render(request, "pages/FAQ.html", context)

def gadgets(request):
    print("Session here:*********")
    print(request.session['loginID'])
    logged = request.session['loginID']

    if logged == "Nothing":
        return redirect('/')

    context = {
        "logged" : logged
    }
    return render(request, "pages/gadgets.html", context)

def checkout(request):
    print("Session here:*********")
    print(request.session['loginID'])
    print(request.POST['quantity'])
    logged = request.session['loginID']

    if logged == "Nothing":
        return redirect('/')

    if logged == "admin":
        user = User.objects.get(id=1)
    else:
        user = User.objects.get(id=logged)

    transaction_id = datetime.datetime.now().timestamp()

    print("transaction-id below")
    print(transaction_id)

    if request.POST['quantity'] == "":
        quantity = 1
    else:
        quantity = request.POST['quantity']

    print("Quantity below: ")
    print(quantity)

    order = Order.objects.create(customer=user, complete=False, transaction_id=transaction_id)
    print(order)

    item = Items.objects.get(id=1)

    orderItem = OrderItem.objects.create(item=item, order=order, quantity=quantity)
    print(orderItem)

    items = order.orderitem_set.all()

    print(items)
        

    context = {
        "logged" : logged,
        "order" : order,
        "items" : items,
        "traId" : transaction_id
    }
    return render(request, "pages/checkout.html", context)

def processOrder(request):
    logged = request.session['loginID']
    data = json.loads(request.body)

    traId = data['traId']
    print("traId here: ")
    print(traId)

    if logged == "admin":
        user = User.objects.get(id=1)
    else:
        user = User.objects.get(id=logged)

    order = Order.objects.get(transaction_id=traId)
    total = float(data['form']['total'])

    if total == order.get_item_total:
        order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer=user,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        country=data['shipping']['country'],
    )
    return JsonResponse('Payment complete', safe=False)

def emailList(request):
    EmailList.objects.create(email=request.POST['email'])
    emailAdded = "Email Added!"
    context = {
        "emailAdded" : emailAdded
    }
    return render(request, "login.html", context)