from os import name
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    return render(request, 'main/index.html')

# product page
def safetywearpage(request):
    data = safetyWears.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)
    try:
        item = paginator.page(page)
    except PageNotAnInteger:
        item = paginator.page(1)
    except EmptyPage:
        item = paginator.page(paginator.num_pages)
    return render(request, 'main/safety_wear/safety_wear_page.html',{'data':item ,"item_paginator":item})

#safety dress view details
def safety_dress_details(request,id):
    item = safetyWears.objects.filter(id=id)
    return render(request, 'main/safety_wear/safety_dress_detail.html', {'item':item})

# safety dress upload
def safety_dress_upload(request):
    form = safetyform()
    if request.method == "POST":
        form = safetyform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('safety_dress_upload')
    else:
        form = safetyform()
  
    img = safetyWears.objects.all()
    return render(request, 'main/safety_wear/safety_wear_upload.html',{'form':form , 'data':img})

#delete the image
def safety_wear_delete(request,id):
    data = safetyWears.objects.get(id=id)
    data.delete()
    return redirect('safety_dress_upload')


# t-shirt page
def tshirtpage(request):
    data = tshirts.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)
    try:
        item = paginator.page(page)
    except PageNotAnInteger:
        item = paginator.page(1)
    except EmptyPage:
        item = paginator.page(paginator.num_pages)
    return render(request, 'main/t-shirt/t_shirt_page.html',{'data':item ,"item_paginator":item})

# t-shirt detail page
def t_shirt_details(request,id):
    item = tshirts.objects.filter(id=id)
    return render(request, 'main/t-shirt/t_shirt_details.html', {'item':item})

# t-shirt uploads
def t_shirt_upload(request):
    form = tshirtform()
    if request.method == 'POST':
        data = tshirtform(request.POST , request.FILES)
        if data.is_valid():
            data.save()
            return redirect('t_shirt_upload')
    else:
        form = tshirtform()
    img = tshirts.objects.all()
    return render(request, 'main/t-shirt/t_shirt_upload.html', {'form':form , 'data':img})

#delete
def t_shirt_delete(request,id):
    data = tshirts.objects.get(id=id)
    data.delete()
    return redirect('t_shirt_upload')

                          #uniforms
# uniform page
def uniformpage(request):
    data = uniforms.objects.select_related().order_by('id') #this select_related is for testing purpose
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)
    try:
        item = paginator.page(page)
    except PageNotAnInteger:
        item = paginator.page(1)
    except EmptyPage:
        item = paginator.page(paginator.num_pages)
    return render(request, 'main/uniform/uniform_page.html',{'data':item ,"item_paginator":item})

# uniform detail page
def uniform_details(request,id):
    item = uniforms.objects.filter(id=id)
    return render(request, 'main/uniform/uniform_details.html', {'item':item})

def uniforms_upload(request):
    form = uniform_form()
    if request.method == 'POST':
        data = uniform_form(request.POST , request.FILES)
        if data.is_valid():
            data.save()
            return redirect('uniforms_upload')
    else:
        form = uniform_form()

    img = uniforms.objects.all()
    return render(request, 'main/uniform/uniforms_upload.html', {'form':form , 'data':img})

def uniform_delete(request,id):
    data = uniforms.objects.get(id=id)
    data.delete()
    return redirect('uniforms_upload')

#caps
def cappage(request):
    data = caps.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 20)
    try:
        item = paginator.page(page)
    except PageNotAnInteger:
        item = paginator.page(1)
    except EmptyPage:
        item = paginator.page(paginator.num_pages)
    return render(request, 'main/caps_flags/caps_flags_page.html',{'data':item ,"item_paginator":item})

# caps detail page
def caps_details(request,id):
    item = caps.objects.filter(id=id)
    return render(request, 'main/caps_flags/caps_flags_details.html', {'item':item})

def cap_upload(request):
    form = cap_form()
    if request.method == 'POST':
        data = tshirtform(request.POST , request.FILES)
        if data.is_valid():
            data.save()
            return redirect('cap_upload')
    else:
        form = cap_form()
    img = caps.objects.all()
    return render(request, 'main/caps_flags/cap_upload.html', {'form':form , 'data':img})

def caps_delete(request,id):
    data = safetyWears.objects.get(id=id)
    data.delete()
    return redirect('cap_upload')


# CONTACT FORM
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('number')
        country = request.POST.get('country')
        address = request.POST.get('addresss')
        city = request.POST.get('city')
        text = request.POST.get('text')
        new_data = contactForm(name=name, email=email, phone_number=phone_number,address=address, country=country, city=city, text=text)
        new_data.save()
    else:
        pass
    return redirect('/')


def contact(request):
    no = contactForm.objects.all()
    return render(request, 'main/admin.html', {'no':no})






# for delete the from the cloud
#  
# from django.db.models.signals import pre_delete
# import cloudinary
# class Photo(models.Model):
#     image = CloudinaryField('image')
#     caption = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return self.caption if self.caption != "" else "No caption"
# @receiver(pre_delete, sender=Photo)
# def photo_delete(sender, instance, **kwargs):
#     cloudinary.uploader.destroy(instance.image.public_id)