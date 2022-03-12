from django import forms
from .models import Internship, Retest, Bonafied, Accepted_students, FinalPDFgeneratedstudents, YourModel
#from home.models import Post

class HomeForm(forms.ModelForm):
    pass

class BonafiedForm(forms.ModelForm):
    class Meta:
        model = Bonafied
        fields = ('name', 'register_number', 'purpose', 'Fa_name', 'proof')

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ('name', 'register_number', 'type', 'Fa_name', 'proof')

class RetestForm(forms.ModelForm):
    class Meta:
        model = Retest
        fields = ('name', 'register_number', 'test', 'subject', 'Fa_name', 'proof')



#
class Accepted_studentsForm(forms.ModelForm):
    class Meta:
        model = Accepted_students
        fields='__all__'
        #field = ('name_a', 'register_number_a', 'test_a', 'type_a', 'subject_a', 'proof_a')

#

class FinalPDFgeneratedstudentsForm(forms.ModelForm):
    class Meta:
        model = FinalPDFgeneratedstudents
        fields = '__all__'


class YourModelForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = '__all__'
