from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, VerifyCodeForm, UserLoginForm
import random
from .models import OptCode, User
from django.contrib import messages
from utils import send_otp_code
import datetime
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class UserRegisterView(View):
    form_class = UserRegisterForm
    temp = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.temp, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            random_code = random.randint(1000, 9999)
            send_otp_code(cd['phone_number'], random_code)
            OptCode.objects.create(phone=cd['phone_number'], code=random_code)
            request.session['user_info'] = {
                'phone_number': cd['phone_number'],
                'email': cd['email'],
                'fullname': cd['fullname'],
                'password': cd['password'],
            }
            messages.success(request, 'we sent you a code', 'success')
            return redirect('accounts:verifycode')
        return render(request, self.temp, {'form': form})
    

class VerifyCodeView(View):
    form_class = VerifyCodeForm
    temp = 'accounts/verifycode.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.temp, {'form': form})    

    def post(self, request):
        user_session = request.session['user_info']
        code_instance = OptCode.objects.get(phone=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            expire = False #create a variable for checking code expire
            #expire time is 2 minutes
            if timezone.now() > code_instance.created + datetime.timedelta(minutes=2):
                expire = True
            if cd['code'] == code_instance.code and not expire:
                User.objects.create_user(phone_number=user_session['phone_number'], email=user_session['email'],
                                         fullname=user_session['fullname'], password=user_session['password'])
                code_instance.delete()
                messages.success(request, 'You Registred', 'success')
                return redirect('home:home')
            elif expire:
                code_instance.delete() #deleting code if it's expired
                messages.error(request, 'Sorry Code has been expired, Try Again', 'danger')
                return redirect('accounts:verifycode')
              
            else:
                messages.error(request, 'Wrong Code', 'danger')
                return redirect('accounts:verifycode')
        return redirect('home:home')
    

class UserLoginView(View):
    form_class = UserLoginForm
    temp = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.temp, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(phone_number=cd['phone_number'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('home:home')
        return render(request, self.temp, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You logged Out!', 'success')
        return redirect('home:home')
