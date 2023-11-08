from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import  never_cache
from django.contrib.auth.decorators import login_required


# Create your views here.

# Home.............! 

@login_required(login_url='Login')
@never_cache
def home(request):
   
    return render(request,'home.html')   

    # admin_home............!
    
@login_required(login_url='admin_login')
@never_cache
def admin_home(requset):
    
    data=User.objects.filter(is_staff=False)
    context={
        'data':data,
    }
    return render(requset,'admin_home.html',context)
  
    
    # admin_login ............!
    
@never_cache
def admin_login(request):
    
    if 'admin' in request.session:
        return redirect('admin_home')
    
    elif  'user'  in request.session:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('Username')
        A_pass1 = request.POST.get('password')
        
        # auth cheking
        
        user = authenticate(request, username=username, password=A_pass1)
        if user is not None and user.is_superuser:
            login(request, user)
            request.session['admin'] = username
           
            return redirect('admin_home')
        else:
        
            return render(request, 'admin_login.html',{'error_msg':' invalid Username or password'})
        
    return render(request,'admin_login.html')

#  Login ...............!


@never_cache
def Login(requset):
    if  'user'  in requset.session:
        return redirect('home')
    
    elif 'admin' in requset.session:
        return redirect('admin_home')

    
    if requset.method == 'POST':
        uname=requset.POST.get('Username')
        pass1=requset.POST.get('password')
        
         #auth checking........!
        
        user= authenticate(requset,username=uname,password=pass1)
        if user is not None:
            login(requset,user)
            requset.session['user']=uname
            return redirect('home')
        else:
            return render(requset,'login.html',{'error_msg':' invalid Username or password'})
                
    return render(requset,'login.html')

    #  signup ........................!
    
@never_cache
def signup(requset):
    
    if  'user'  in requset.session:
        return redirect('home')
    
    elif 'admin' in requset.session:
        return redirect('admin_home')

    if requset.method =='POST':
        uname=requset.POST.get('Username')
        email=requset.POST.get('email')
        pass1=requset.POST.get('password')
        pass2=requset.POST.get('con_password')
        
        # auth checking
        
        if not (uname and email and pass1 and pass2) :
          return render(requset,'signup.html',{'error_all':" Please fill required fields"})
        elif User.objects.filter(username=uname).exists():
            return render(requset,'signup.html',{'error_uname':'Username already exists'})
        elif User.objects.filter(email=email).exists():
            return render(requset,'signup.html',{'error_email':'Email already exists'})
        elif pass1 != pass2:
            return render(requset,'signup.html',{'error_pass':'passwords mismatch'})
        else:
            my_user=User.objects.create_user(username=uname,email=email,password=pass1)
            my_user.save()
            return redirect('Login')


    return render(requset,'signup.html')

       

    # Logout.................!

@never_cache
def Logout(requset):
    if 'user' in requset.session:
        requset.session.flush()
        logout(requset)
        return redirect('Login')
    
    # admin_logout..............!
    
@never_cache
def admin_Logout(requset):
    
    if  'admin' in requset.session:
        requset.session.flush()
        logout(requset)
        return redirect('admin_login')
    
    # adding data .............!
    
def add(request):
    
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        if User.objects.filter(username=name).exists():
            
            return render(request,'alert.html')
           
           
        else:
            user=User.objects.create_user(username=name,email=email,password=password)
            user.save()
            return redirect('admin_home')
        
    return render(request,'admin_home.html')

   # edit .............!
   
def edit(request):
    
   users=User.objects.all()
   
   context={
       
       'data':users
   }    
       
   return render(request,'admin_home.html',context)
 
 # update ................!
 
def update(request,id):
     
    if request.method == 'POST':
         
        name=request.POST.get('name')
        email=request.POST.get('email')
        user=User.objects.create_user(id=id,username=name,email=email)
        user.save()
        return redirect('admin_home')
    
    return render(request,'admin_home.html')
         
        # delete .............!
         
def delete(request,id):
    
    data=User.objects.filter(id=id)
    data.delete()
    
    return redirect('admin_home')

   # search ................!

def search(request):
    
    if 'q' in request.GET:
        q=request.GET['q']
        data = User.objects.filter(username__icontains=q)
        context={
            'data':data
        }
        
    return render(request,'admin_home.html',context)

    # alert...............!
    
def alert(request):
    return redirect('admin_home')