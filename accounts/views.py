from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView

from accounts.forms import (
    RegistrationForm,
    TeacherRegistrationForm,
    HODRegistrationForm,
    EditProfileForm
)

#from django.contrib.auth.models import User     uncomment to get the old back
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from accounts.models import User

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))
    else:
        form = RegistrationForm()

    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)



##remove to get back the old.

def Teacherregister(request):
    if request.method =='POST':
        form = TeacherRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))
    else:
        form = TeacherRegistrationForm()

    args = {'form': form}
    return render(request, 'accounts/teacherreg_form.html', args)
##



##
def hodregister(request):
    if request.method =='POST':
        form = HODRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))
    else:
        form = HODRegistrationForm()

    args = {'form': form}
    return render(request, 'accounts/hodreg_form.html', args)
##


##
class SignUpView(TemplateView):
    template_name = 'accounts/signup.html'
##


##remove to get the old back
#class StudentSignUpView(CreateView):
    #model = User
    #form_class = RegistrationForm
    #template_name = 'registration/signup_form.html'

    #def get_context_data(self, **kwargs):
    #    kwargs['user_type'] = 'student'
    #    return super().get_context_data(**kwargs)

    #def form_valid(self, form):
    #    user = form.save()
    #    login(self.request, user)
    #    return redirect('students:quiz_list')
##


##remove to get the old back
#class TeacherSignUpView(CreateView):
    #model = User
    #form_class = TeacherRegistrationForm
    #template_name = 'registration/signup_form.html'

    #def get_context_data(self, **kwargs):
    #    kwargs['user_type'] = 'teacher'
    #    return super().get_context_data(**kwargs)

    #def form_valid(self, form):
    #    user = form.save()
    #    login(self.request, user)
    #    return redirect('teachers:quiz_change_list')
##




def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            #return redirect(reverse('accounts:view_profile'))
            return redirect(reverse('home:home'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_passwords'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
