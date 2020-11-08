from django.shortcuts import render,redirect
from django.views.generic import TemplateView ,View
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib.auth import authenticate , logout ,login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/home.html'


class About(TemplateView):
    template_name = 'main/about.html'

class UserRegistations(View):
    def get(self,request,*args,**kwargs):
        form = UserForm()
        data = {"form":form}
        return render(request,'user/registations.html',data)

    def post(self,request,*args,**kwargs):
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('registations')


class UserLogin(View):
    def get(self,request,*args,**kwargs):
        return render(request,'user/login.html')

    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        cond = Q(contact = username ) & Q(password = password)
        check = User.objects.filter(cond).count()

        if (check == 1):
            request.session['userlogin'] = username
            return redirect('dashaboard')
        else:
            return redirect('user_login')

class Dashaboard(View):
    def get(self, request, *args, **kwargs):
        if not request.session.has_key('userlogin'):
            return redirect('user_login')

        id = User.objects.get(contact=request.session['userlogin']).user_id

        content = {
            "panding": Service.objects.filter(user_id=id, status='panding').count(),
            "select": Service.objects.filter(user_id=id, status='apsept').count(),
            "reject": Service.objects.filter(user_id=id, status='reject').count()
        }
        return render(request, 'user/dashaboard.html', content)


class ApplyNewService(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('userlogin'):
            return redirect('user_login')

        form = ServiceForm()
        data = {"form":form}
        return render(request,'user/apply_service.html',data)

    def post(self,request,*args,**kwargs):
        if not request.session.has_key('userlogin'):
            return redirect('user_login')

        id = User.objects.get(contact = request.session['userlogin']).user_id
        form = ServiceForm(request.POST or None)
        if form.is_valid():
            a = form.save(commit=False)
            a.user_id = User(id)
            a.status = 'panding'
            a.save()
            return redirect('dashaboard')
        else:
            return redirect('applynewsevice')


class PandingRequest(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('userlogin'):
            return redirect('user_login')
        id = User.objects.get(contact = request.session['userlogin']).user_id
        data = Service.objects.filter(user_id = id , status = 'panding')
        content = {'panding':data}
        return render(request,'user/panding_service.html',content)


class AproveRequest(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('userlogin'):
            return redirect('user_login')
        id = User.objects.get(contact = request.session['userlogin']).user_id
        data = Service.objects.filter(user_id = id , status = 'apsept')
        content = {'select':data}
        return render(request,'user/selected_sevice.html',content)


class RejectRequest(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('userlogin'):
            return redirect('user_login')
        id = User.objects.get(contact = request.session['userlogin']).user_id
        data = Service.objects.filter(user_id = id , status = 'reject')
        content = {'reject':data}
        return render(request,'user/rejected_sevice.html',content)


class UserLogout(View):
    def get(self,request,*args,**kwargs):
        if request.session.has_key('userlogin'):
            del request.session['userlogin']
            return render(request,'user/login.html')



#----------------------------------------------------------- ADMIN WORK ----------------------------------------------#


class AdminLogin(View):
    def get(self,request):
        return render(request,'admins/login.html')

    def post(self,request,*args,**kwargs):

        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username = username , password = password)

            if user is not None:
                login(request,user)
                return redirect('requestservice')
            else:
                return redirect('admin_login')



class AdminDashaboard(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        content = {
            "requestservices":Service.objects.filter(status='panding').count(),
        }
        return render(request,'admins/dashaboard.html',content)


class RequestSevice(LoginRequiredMixin,View):
    def get(self,request):
        content = {
            "requestservices":Service.objects.filter(status='panding'),
        }
        return render(request,'admins/all_request.html',content)


class AproveService(LoginRequiredMixin,View):
    def get(self,request,pk,*args,**kwargs):
        data = Service.objects.get(service_id=pk)
        data.status = 'apsept'
        data.save()
        return redirect('requestservice')


class Servicing(LoginRequiredMixin,View):
    def get(self, request):
        content = {
            "apseptservices": Service.objects.filter(status='apsept'),
        }
        return render(request,'admins/apseptservice.html', content)


class Complite(View):
    def get(self,request,pk,*args,**kwargs):
        data = Service.objects.get(service_id=pk)
        data.status = 'complite'
        data.save()
        return redirect('requestservice')


class ComplateServicing(LoginRequiredMixin,View):
    def get(self, request):
        content = {
            "complite": Service.objects.filter(status='complite'),
        }
        return render(request,'admins/all_complete_service.html', content)


class AdminLogout(View):
    def get(self,request):
        logout(request)
        return render(request,'main/home.html')



