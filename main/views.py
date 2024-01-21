from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

def main(request):

    body=models.Body.objects.all()
    sinf=models.Class.objects.all()
    mashgulot=models.Mashgulot.objects.all()
    teacher=models.Teacher.objects.all()
    service=models.Service.objects.all()
    contact=models.Contact_Us.objects.all()

    context={
        "body":body,
        "sinf":sinf,
        "mashgulot":mashgulot,
        "teacher":teacher,
        "service":service,
        "contact":contact
    }
    return render(request,'asosiy/index.html',context)




#dashboard

def dashboard(request):
    
    return render(request,'dashboard/index.html')




# Body

def body_create(request):
    icon=request.FILES.get('image')
    name=request.POST.get('name')
    body=request.POST.get('body')
    if request.method=='POST':
        models.Body.objects.create(
            icon=icon,
            name=name,
            body=body

       )
        return redirect('body')
    return render(request,'dashboard/body/create.html')



def body(request):
    bodies=models.Body.objects.all()
    context={
        'bodies':bodies
    }
    print(context)
    return render(request,'dashboard/body/list.html',context)


def body_update(request,id):
    bodies=models.Body.objects.get(id=id)
    if request.method=='POST':
        bodies.body=request.POST=['body']
        bodies.name=request.POST=['name']
        icon=request.ILES.get('image')
        if icon:
            bodies.icon=icon
            bodies.save()


    context={
        'bodies':bodies
    }

    return render(request,'dasgboard/body/update.html',context)


def body_delete(request):
    body=models.Body.objects.get(id=id).delete()
    return  redirect(body)


#class


def class_create(request):
    icon=request.FILES['icon']
    name=request.POST['name']
    teacher=request.POST['teacher']
    if request.method=='POST':
        models.Class.objects.create(
            icon=icon,
            name=name,
            teacher=teacher
        )
        return redirect('classes')
    return render(request,'dashboard/class,create.html')


def classes(request):
    classes=models.Class.objects.all()
    context={
        'classes':classes
    }

    return render(request,'dashboard/class/list.html',context)



def class_update(request,id):
    classes=models.Class.objects.get(id=id)
    if request.method=='POST':
        classes.teacher=request.POST=['teacher']
        classes.name=request.POST=['name']
        icon=request.ILES.get('image')
        if icon:
            classes.icon=icon
        classes.save()


    context={
        'classes':classes
    }

    return render(request,'dasgboard/body/update.html',context)


def class_delete(request,id):
    if request.method=='POST':
        models.Class.objects.get(id=id).delete()

        return redirect('classes')
    






# Teacher
    

def teacher_create(request):
    image=request.FILE['image']
    name=request.POST['name']
    haqida=request.POST['haqida']
    if request.method=='POST':
        models.Teacher.objects.create(
            image=image,
            name=name,
            haqida=haqida

       )
        return redirect('teachers')
    return render(request,'dashboard/teacher/create.html')



def teachers(request):
    teachers=models.Body.objects.all()
    context={
        'teachers':teachers
    }
    return render(request,'dashboard/teacher/list.html',context)


def teacher_update(request,id):
    teachers=models.Teacher.objects.get(id=id)
    if request.method=='POST':
        teachers.haqida=request.POST['haqida']
        teachers.name=request.POST['name']
        image=request.FILES.get('image')
        if image:
            teachers.image=image
        teachers.save()


    context={
        'teachers':teachers
    }

    return render(request,'dasgboard/teacher/update.html',context)


def teacher_delete(request,id):
    models.Teacher.objects.get(id=id).delete()
    return  redirect(teachers)


#Service

def service_create(request):
    service_icon=request.POST.get('image')
    service_name=request.POST.get('name')
    about_service=request.POST.get('about')

    if request.method=='POST':

        models.Service.objects.create(
            service_icon=service_icon,
            service_name=service_name,
            about_service=about_service
          )
        return redirect('services')
    return render(request,'dashboard/service/create.html')




def services(request):
    services=models.Service.objects.all()
    context={
        'services':services

    }
    return render(request,'dashboard/service/list.html',context)


def service_update(request,id):
    services=models.Service.objects.get(id=id)

    if request.method=='POST':
        services.service_icon=request.POST.get('image')
        services.service_name=request.POST['name']
        about_service=request.POST['about']

        if about_service:
            services.about_service

        services.save()
    return render(request,'dashboard/service/update.html')

def service_delete(request,id):
    models.Service.objects.get(id=id).delete()
    return  redirect(services)







#authentication

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'dashboard/auth/register.html', {'error': 'Username and password are required.'})

        try:
            user = User.objects.create_user(username=username, password=password)
            
            return redirect('dashboard')  
        except Exception as e:
            return render(request, 'dashboard/auth/register.html', {'error': str(e)})

    return render(request, 'dashboard/auth/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect(dashboard)  
    return render(request, 'dashboard/auth/login.html')