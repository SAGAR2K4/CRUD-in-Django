from django.shortcuts import redirect,HttpResponse,render
from .models import Member
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    mem = Member.objects.all()
    return render(request, 'index.html',{'mem':mem})


def add(request):
    return render(request,'add.html')


def addrec(request):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['degree']
    d = request.POST['semester']
    e = request.POST['division']
    mem = Member(firstname=x,lastname=y,degree=z,semester=d,division=e)
    mem.save()
    return redirect('index.html')

def delete(request,id) :
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect('index.html')

def update(request,id) :
    mem = Member.objects.get(id=id)
    return render(request,'update.html',{'mem': mem})
    
def uprec(request,id):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['degree']
    d = request.POST['semester']
    e = request.POST['division']
    mem = Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.degree=z
    mem.semester=d
    mem.division=e
    mem.save()
    return redirect('index.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index.html')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')
    
def LogoutPage(request):
    logout(request)
    return redirect('login')
