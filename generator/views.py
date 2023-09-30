from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request,'generator/home.html')
def password(request):
    ln=int(request.GET.get('length'))
    pass1=''
    lc="abcdefghijklmnopqrstuvwxyz"
    uc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sc="!@#$%^&*_-=+"
    nc="0123456789"
    c=""
    if(request.GET.get('lowercase')=="on"):
        pass1+=random.choice(lc)
        c+=lc
    if(request.GET.get('uppercase')=="on"):
        pass1+=random.choice(uc)
        c+=uc
    if(request.GET.get('Special')=="on"):
        pass1+=random.choice(sc)
        c+=sc
    if(request.GET.get('Numbers')=="on"):
        pass1+=random.choice(nc)
        c+=nc
    ln1=len(pass1)
    ln=ln-ln1
    for i in range(ln):
        pass1+=random.choice(c)
    pass2=list(pass1)
    random.shuffle(pass2)
    pass1=''.join(pass2)
    return render(request,'generator/password.html',{'password':pass1})
def about(request):
    return render(request,'generator/about.html')
