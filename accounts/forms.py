from django import forms
import re
#from django.contrib.auth.models import User     uncomment to get the old back
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User  #remove to get the old back
from django.db import transaction       #remove to get the old back

#fa = User.objects.filter(user_type=1)
fa = User.objects.filter(user_type=2)

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    username = forms.RegexField(regex=re.compile(r'^RA[0-9]{13}$'), required=True)  #make it reagex field, change it's name to id number and give your regex
    first_name=forms.CharField(required=True)
    department=forms.CharField(required=True)   ##remove to get the old back
    #last_name=forms.CharField(required=True)
    #u2 = u['user_type'== 2 ]
    #facultyadvisor = forms.ModelChoiceField(queryset=fa, empty_label=None)     #field1 = forms.ModelChoiceField(queryset=User.objects.get(user_type=2))
    #fa_name = forms.ForeignKey(User)

    class Meta(UserCreationForm.Meta):
        model=User
        fields=[
            'image',
            'username',

            #'last_name',
            'email',
            'department',
            'facultyadvisor',
            'password1',
            'password2'
        ]

    @transaction.atomic                            ##remove to get the old back
    def save(self, commit=True):
        user=super(RegistrationForm, self).save(commit=False)
        #user.is_student = True
        user.user_type=1                                 ##remove to get the old one back
        user.first_name=self.cleaned_data['first_name']
        #user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        user.department = self.cleaned_data['department']
        user.facultyadvisor = self.cleaned_data['facultyadvisor']

        if commit:
            user.save()
        return user

## remove to get the old
##Teacher registeration form

class TeacherRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    username = forms.RegexField(regex=re.compile(r'^10[0-9]{4}$'), required=True)  #make it reagex field, change it's name to id number and give your regex
    first_name=forms.CharField(required=True)
    department=forms.CharField(required=True)
    #last_name=forms.CharField(required=True)
    #facultyadvisor=forms.CharField(required=False)

    class Meta(UserCreationForm.Meta):
        model=User
        fields=[
            'image',
            'username',

            #'last_name',
            'email',
            'department',
            #'facultyadvisor',
            'password1',
            'password2'
        ]

    @transaction.atomic                            ##remove to get the old back
    def save(self, commit=True):
        user=super(TeacherRegistrationForm, self).save(commit=False)
        #user.is_teacher = True
        user.user_type=2                                   ##remove to get the old one back
        user.first_name=self.cleaned_data['first_name']
        #user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        user.department = self.cleaned_data['department']
        #user.facultyadvisor = self.cleaned_data['facultyadvisor']

        if commit:
            user.save()
        return user
##



##
class HODRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    username = forms.RegexField(regex=re.compile(r'^100[0-9]{3}$'), required=True)  #make it reagex field, change it's name to id number and give your regex
    first_name=forms.CharField(required=True)
    #last_name=forms.CharField(required=True)
    department=forms.CharField(required=True)
    #facultyadvisor=forms.CharField(required=False)
    class Meta(UserCreationForm.Meta):
        model=User
        fields=[
            'image',
            'username',
            'first_name',
            #'last_name',
            'email',
            'department',
            #'facultyadvisor',
            'password1',
            'password2'
        ]

    @transaction.atomic                            ##remove to get the old back
    def save(self, commit=True):
        user=super(HODRegistrationForm, self).save(commit=False)
        #user.is_teacher = True
        user.user_type=3                                       ##remove to get the old one back
        user.first_name=self.cleaned_data['first_name']
        #user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        user.department = self.cleaned_data['department']
        #user.facultyadvisor = self.cleaned_data['facultyadvisor']

        if commit:
            user.save()
        return user
##


        ##
    ## @transaction.atomic
    ##def save(self):
    ##    user = super().save(commit=False)
    ##    user.is_student = True
    ##    user.save()
    ##    student = Student.objects.create(user=user)
    ##    student.interests.add(*self.cleaned_data.get('interests'))
    ##    return user
        ##






class EditProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields=[
            'image',
            'first_name',
            'password',
            'email',
        ]
