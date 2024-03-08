from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def home(request):
    try:
        fullname=request.session['Name']
        return render(request,'app/home.html',{'data':fullname})
    except:
        return render(request,'app/home.html')


# def base(request):
#     return render(request,'app/base.html')

def Signup(request):
    try:
        fullname=request.session['Name']
        return render(request,'app/register.html',{'data':fullname})
    except:
        return render(request,'app/register.html')

def Login(request):
    try:
        fullname=request.session['Name']
        return render(request,'app/login.html',{'data':fullname})
    except:
        return render(request,'app/login.html')

def about(request):
    try:
        fullname=request.session['Name']
        return render(request,'app/about.html',{'data':fullname})
    except:
        return render(request,'app/about.html')


def savedata(request):
    name=request.POST['Name']
    email=request.POST['email']
    contact=request.POST['number']
    city=request.POST['city']
    password=request.POST['password']

    request.session['Name']=name
    request.session['E-mail']=email
    request.session['Contact']=contact
    request.session['City']=city
    request.session['Password']=password
    
    return render(request,'app/login.html')

def Login_data(request):
    if request.POST:
        email=request.POST['email']
        pwd=request.POST['password']


        if 'E-mail' in request.session:
            emailid=request.session['E-mail']
            pswd=request.session['Password']
            
            if email==emailid and pwd==pswd:
                name=request.session['Name']
                request.session.modified= True 

                return render(request,'app/home.html',{'data':name})
            else:
                ms="Incorrect password or E-mail"
                return render(request,'app/login.html',{'incoreectmsg':ms})
        else:
            msg = "Either Session expired or sessionid not set..........."
            return render(request,'App/register.html',{'msg1':msg})   
    else:
        msg1 = "Session expired..........."
        return render(request,'app/register.html',{'msg1':msg1})


def delete(request):
    if 'Name' in request.session:
        del request.session['Name']
        request.session.flush()
   
    return render(request,'app/register.html')
