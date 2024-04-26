from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Reg
# Create your views here.

class Home(View):
    def get(self, request):
        return render(request,'home.html')
class RegisterInput(View):
    def get(self, request):
        return render(request, 'register.html')

class Register(View):
    def post(self, request):
        r1 = Reg(fname=request.POST.get('firstname'),
               lname=request.POST.get('lastname'),
               email=request.POST.get('email'),
               mobile=request.POST.get('mobile'),
               dob=request.POST.get('dob'),
               username=request.POST.get('username'),
               password=request.POST.get('password'),
               cpassword=request.POST.get('confirmpassword'))
        r1.save()
        return HttpResponse('Your are successfully registered')
class LoginInput(View):
    def get(self, request):
        return render(request,'login.html')

class Login(View):
    def post(self, request):
        qs=Reg.objects.filter(username=request.POST.get('username'),
                              password=request.POST.get('password'))
        if qs:
            return HttpResponse('Login success')
        else:
            return HttpResponse('Login failed')
