from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpRequest
import random
from .models import *
from django.contrib.auth.models import User,auth
# Create your views here.
li=[]
ress=[]

def cal(requset,s=0):
    h=Fun.objects.all().values()
    if s==0:
        lis=[]
        for i in range(0,15):
            res=random.choice(h)
            lis.append(res)
        li=random.sample(lis,10) 
        res=[]
        for i in li:
            r=(i.values())
            k=0
            for j in r:
                if (k==0 or k==6):
                    res.append(j)
                k+=1
        ress.append(res)
    return render(requset,'result.html',{'outer':li ,'out1':res,})

def good(requset):
    return render(requset,'first.html',)

def bios(requset):
    if requset.method =='POST':
        name=requset.POST['name']
        fun = Fun(quest=name,cho1='g',cho2='fg',cho3='ghj',cho4='gjhg',ans='g')
        fun.save()
        return redirect('/')
    else:
        return render(requset,'save.html')

def save(request):
    sc=request.POST['score']
    data.objects.filter(name='gokul').update(score=sc)
    pr = data.objects.all(id=1)
    print(pr)
    return redirect('/')
    

def res(request):
    
    lis=request.POST['list']
    #user values
    uname=request.POST['uname']
    datas=data.objects.all().values()
    pr = data.objects.all().filter(name=uname)
    a=pr[0]
    a=str(a)
    if len(a)>=16:
        a=a[13]+a[14]
    else:
        a=(a[13])

    ind=int(a)
    
    uda=[]
    k=1
    for i in datas:
            r=(i.values())
            save='f'
            for j in r:
                if j==ind and k==1:
                    save='t'
                    k=2
                if save=='t':
                    uda.append(j)

                
    att=uda[3]
    #calculate
    lis1=[]
    app=""
    for i in lis:
        if i=="[" or i=="," or i==']':
            if app!="":
                lis1.append(app)
                app=""
        elif i=="'" or i==" ":
            continue
        else:
            app+=i

    #score
    a=0
    anser=[]
    
    for i in range(0,len(lis1),2):
        ch=request.POST[lis1[i]]
        if lis1[i+1]==ch:
            a+=1
        anser.append(ch)
    sco=uda[2]
    ps= 25.12*(uda[2]/10)
    ps1=251.2-ps
    s=25.12*a
    s1=251.2-s
    a*=10
    att+=1
    data.objects.filter(name=uname).update(score=a,at=att)
    return render(request,'index.html',{'re':att,'score':s,'score2':s1,'sco':a,'pscore':ps,'pscore1':ps1,'psco':sco})

   

#login functions

def web(request):
    
    return render(request,'webshare.html',{'new':'hello'})
    
def sign(request):
    if request.method == 'POST':
        username = request.POST['name1']
        password = request.POST['password3']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            uname=username
            print(uname)
            auth.login(request,user)
            return redirect('/')
        else:
            message = 'invaled username or password'
            return render(request,'signin.html',{'message':message})
    else:
        return render(request,'signin.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        firstname = request.POST['name1']
        secondname = request.POST['name1']
        password = request.POST['password1']
        repassword=request.POST['password2']
        if password==repassword:
            if User.objects.filter(username=username).exists():
                message1 = 'username is taken'
                return render(request,'login.html',{'messageus':message1})
            else:
                user = User.objects.create_user(username=username,password=password,first_name=firstname,last_name=secondname)
                user.save()
                dat= data()
                dat.name=username
                dat.score=0
                dat.at=0
                dat.save()
                print('user created')
                return redirect('/sign')
        else:
            message2 = 'password is not correct'
            return render(request,'login.html',{'message':message2})
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

"""def save(request):
    if request.method == 'POST':
        pro =Calc()
        pro.quest=request.POST['nameim']
        pro.cho1=request.POST['cho1']
        pro.cho2=request.POST['cho2']
        pro.cho3=request.POST['cho3']
        pro.cho4=request.POST['cho4']
        pro.ans=request.POST['ans']
        pro.save()
        calc = Calc.objects.filter(id=1).update(quest="dinesh",ans="g")
        #pro.objects.create_calc()
        
        return redirect("/")
    else:
        return render(request,'save.html')
"""
    

