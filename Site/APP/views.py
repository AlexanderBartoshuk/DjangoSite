import os
from django.http import FileResponse, Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from random import randint 
from APP.models import*




def hello_world(request):
    return HttpResponse("Hello World")
def random_page(request):
    return HttpResponse(f"Случайное число : {randint(0,100)}")
 

def page1(request):
    return HttpResponse("Эта страница page1")

def page2(request):
    return HttpResponse("Эта страница page2")

def page3(request):
    return HttpResponse("Эта страница page3")

def products_page(request):
    return HttpResponse("<h1>Наши продукты</h1>")

def pages(request, id):
    return HttpResponse(f"<h1> Это страница {id} </h1>")

def user(request):
    name = request.GET.get("name")
    age = request.GET.get('age')
    if int(age) in range (1,99):
        if int(age) < 14:
            return HttpResponse(f"<h2>Имя : {name} Возраст : {age}")
        else:
            return HttpResponse(f"<h2>Имя : {name} Возраст : {age}")

def file_show(request):
    return FileResponse(open('APP/images/20190519_114158.jpg' , 'rb'),
                as_attachment= True,
                        filename='code20190519_114158.jpg')         

def file_1(request):
    return FileResponse(open('APP/images/1.jpg' , 'rb'))

def file_2(request):
    return FileResponse(open('APP/images/2.jpg' , 'rb')) 

def file_3(request):
    return FileResponse(open('APP/images/3.jpg' , 'rb')) 

def files (request, id):
    directory = 'APP\images'
    number = len(os.listdir(directory))
    if id == 0:
        raise Http404()
    elif id <= number:
        return FileResponse(open(f'APP/images/{id}.jpg' , 'rb'))
    else:
        raise Http404() 

def json_work(request):
    data = {'prise':100, 'title': 'book1'}
    return JsonResponse(data) 


def main_page(request):
    return render(request, 'main.html')


def info_page(request):
    return render(request, 'info.html')

def products_page(request):
    bd = list(Products.objects.all())
    return render(request, 'products.html', {'products' : bd})

def work_page(request):
    return render(request, "work.html")

def course_page(request):
    return render(request, "course.html")

def hour_page(request):
    return render(request, "hour.html")

def materials_page(request):
    return render(request, "materials.html")

def payment_page(request):
    return render(request, "payment.html")

def person_page(request):
    return render(request, "person.html")

def end_page(request):
    return render(request, "end.html")

def the_page(request):
    return render(request, 'register.html')

def app_client(request):
    name = request.GET.get('name' , '')
    number = request.GET.get('number' , '')
    print("name" ) 
    return render(request, 'create_client.html')

def display_view(request):
    name = request.GET.get('name') 
    phone = request.GET.get('phone') 
    print(name , phone)
    return render(request, 'create_client.html')


def display_page(request):
        return render(request, 'create_client.html')

from django.shortcuts import render, redirect
from .forms import ClientForm

def app_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # перенаправляем на главную страницу после успешной отправки формы
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})









