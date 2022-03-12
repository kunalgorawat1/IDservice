
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
#from django.contrib.auth.models import User        uncomment to get bak to old

from home.forms import HomeForm, InternshipForm, RetestForm, BonafiedForm, Accepted_studentsForm, FinalPDFgeneratedstudentsForm, YourModelForm
from home.models import Student, User, Internship, Retest, Bonafied, Accepted_students, FinalPDFgeneratedstudents, YourModel       #I've removed Post from models so remove here as well and added User which is an extended class in models and auth.models's User wount work.
from django.core.mail import send_mail     #dosen't hurt but remove to get the old back.
from django.core.files.storage import FileSystemStorage



from django.http import HttpResponse
from django.views.generic import View

from home.utils import render_to_pdf #created in step 4

from time import ctime

from django.core.files import File

from io import BytesIO

class HomeView(TemplateView):
    template_name = 'home/home.html'

#this get method takes entry from the post form as a get request
    def get(self, request):
    #    form = HomeForm()
    #    posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        users_fa = User.objects.exclude(user_type=3)
        users_hod = User.objects.exclude(user_type=2)
        #student = Student.objects.get(current_user=request.user)

        students = Student.objects.all()

        #students = student.users.all()

        args = {
             'users': users, 'users_fa':users_fa, 'users_hod':users_hod, 'students':students                         #'form': form, 'posts': posts, 'users': users, 'students': students
        }
        return render(request, self.template_name, args)                                    #uncommnet to get back to old


#
#And this post method posts it to the server
    #def post(self, request):
    #    form = HomeForm(request.POST)
    #    if form.is_valid():
    #        post = form.save(commit=False)
    #        post.user = request.user
    #        post.save()

    #        text = form.cleaned_data['post']
    #        form = HomeForm()
    #        return redirect('home:home')

    #    args = {'form': form, 'text': text}
    #    return render(request, self.template_name, args)                                   #uncommnet to get back to old


def change_students(request, operation, pk):
    student = User.objects.get(pk=pk)
    if operation == 'add':
        Student.make_student(request.user, student)
    elif operation == 'remove':
        Student.loose_student(request.user, student)
    return redirect('home:home')


def change_facultyadvisor(request, operation, pk):
    fastudents= User.objects.get(pk=pk)
#def send_request(request, operation, pk):





def send_mail_to_fa(self):
    send_mail(
        'New request on the service app',
        'please login to access the new request your account has got recently.',
        'admin@gmail.com',
        ['faculty_advisor@gmail.com'],
        fail_silently=False,
        )


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    #  delete to get the old
    context={}
    retests = Retest.objects.all()
    internships =Internship.objects.all()
    context['retests']=retests
    context['internships']=internships#
    context['user']=user
    #
    #args = {'user': user, 'retests':retests, 'internships':internships}
    return render(request, 'home/home.html', context)


##
#def bonafied_certificate(request, pk=None):
#    context = {}
#    if request.method == 'POST':
#        upload_file = request.FILES['document']
#        fs = FileSystemStorage()
#        name = fs.save(upload_file.name, upload_file)
#        context['url'] = fs.url(name)
#    return render(request, 'home/bonafied_certificate_upload.html', context)

##
def upload_bonafied_form(request):
    if request.method == 'POST':
        form = BonafiedForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            faname = request.user.facultyadvisor
            mail = User.objects.filter(first_name=faname).values('email')
            mail = mail.first()
            mail = mail['email']
            send_mail(
                'New request on the service app',
                'please login to access the new request your account has got recently.',
                'admin@gmail.com',
                [mail],
                fail_silently=False,
                )

            return redirect('home:retest_list')
    else:
        form = BonafiedForm(initial={'Fa_name': request.user.facultyadvisor})
    return render(request, 'home/upload_bonafied_form.html', { 'form' : form })
##
##
#def Internship(request, pk=None):
#    context = {}
#    if request.method == 'POST':
#        upload_file = request.FILES['document']
#        fs = FileSystemStorage()
#        name = fs.save(upload_file.name, upload_file)
#        context['url'] = fs.url(name)
#    return render(request, 'home/Internship.html', context)

##
#def Retest(request, pk=None):
#    context = {}
#    if request.method == 'POST':
#        upload_file = request.FILES['document']
#        fs = FileSystemStorage()
#        name = fs.save(upload_file.name, upload_file)
#        context['url'] = fs.url(name)
#    return render(request, 'home/Retest.html', context)
#
####


def retest_list(request, pk=None):

    #
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    #

    context = {}
    retests = Retest.objects.all()
    internships =Internship.objects.all()
    bonafieds = Bonafied.objects.all()

    users_all = User.objects.all()

    context['retests']=retests
    context['internships']=internships
    context['bonafieds']=bonafieds
    context['user']=user
    #
    context['users_all']=users_all
    #context['form']=form

    if request.method == 'POST':
        form = Accepted_studentsForm(request.POST)
        if form.is_valid():
            form.save()

            #send_mail(
            #    'New request on the service app',
            #    'please login to access the new request your account has got recently.',
            #    'admin@gmail.com',
            #    ['HOD@gmail.com'],
            #    fail_silently=False,
            #    )

        else:
            print("You're messed up")
    return render(request, 'home/Retest.html', context)
####


def upload_retest_form(request, pk=None):

    if request.method == 'POST':
        form = RetestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            faname = request.user.facultyadvisor
            mail = User.objects.filter(first_name=faname).values('email')
            mail = mail.first()
            mail = mail['email']
            #send_mail(
            #    'New request on the service app',
            #    'please login to access the new request your account has got recently.',
            #    'admin@gmail.com',
            #    [mail],
            #    fail_silently=False,
            #    )
            return redirect('home:retest_list')
    else:
        form = RetestForm(initial={'Fa_name': request.user.facultyadvisor})
    return render(request, 'home/upload_retest_form.html', { 'form' : form })
##


##

def upload_internship_form(request):
    if request.method == 'POST':
        form = InternshipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            faname = request.user.facultyadvisor
            mail = User.objects.filter(first_name=faname).values('email')
            mail = mail.first()
            mail = mail['email']
            send_mail(
                'New request on the service app',
                'please login to access the new request your account has got recently.',
                'admin@gmail.com',
                [mail],
                fail_silently=False,
                )

            return redirect('home:retest_list')
    else:
        form = InternshipForm(initial={'Fa_name': request.user.facultyadvisor})
    return render(request, 'home/upload_internship_form.html', { 'form' : form })
##


#####
def accepted_students_view(request):
    ##
    if request.method == 'POST':
        form = Accepted_studentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:Retest.html')
    else:
        form= Accepted_studentsForm()
    return render(request, 'home/Retest.html', { 'form': form })
    ##
#####


def onlyforhod_view(request):
    a = Accepted_students.objects.all()
    users_all = User.objects.all()
    if request.method == 'POST':
        form = FinalPDFgeneratedstudentsForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            print("You're messed up")
    return render(request, 'home/onlyforhod.html', {'a':a, 'users_all': users_all})
#def AS(request):
#    AStudents.name = request.POST['name']
#    AStudents.register_n = request.POST['register_n']
#    AStudents.proof = request.FILES['proof']
#    AStudents.type = request.POST['type']
#    AStudents.subject = request.POST['subject']
#    AStudents.test = request.POST['test']


def generate_pdfs_view(request):
    f = FinalPDFgeneratedstudents.objects.all()
    ##
    #pdf = render_to_pdf('home/pdfformat.html', context)
    ##
    ##

    if request.method == 'POST':
        form = YourModelForm(request.POST)

        n = request.POST['name']
        r = request.POST['register_number']
        t = request.POST['type']
        s = request.POST['subject']
        te = request.POST['test']
        p = request.POST['purpose']
        date = ctime()
        context={
            'n':n,
            'r':r,
            't':t,
            's':s,
            'te':te,
            'p':p,
            'date':date
        }

        if form.is_valid():
            form.save()


        pdf = render_to_pdf('home/pdfformat.html', context )
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        form = YourModelForm()
    #obj = YourModel.objects.all()
    ##
        return render(request, 'home/generate_pdfs.html', {'f': f, 'form':form })


def generate_pdfs_actual(request, pk=None, *args, **kwargs):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    f = FinalPDFgeneratedstudents.objects.all()
    date = ctime()

    for j in f:
        context = {
             'j': j,
             'user':user,
             'date':date
        }
        pdf = render_to_pdf('home/pdfformat.html', context)
    return HttpResponse(pdf, content_type='application/pdf')







##
#def generate_obj_pdf(request):
    #rname = request.user.first_name
    #obj = YourModel.objects.all()
    #obj = YourModel.objects.get(id=instance_id)
    # context = {'instance': obj}
#    user = request.user
#    date = ctime()
#    f = FinalPDFgeneratedstudents.objects.all()
#    for j in f:
#        pdf = render_to_pdf('home/pdfformat.html', {'j':j, 'user':user})
#        p = YourModel(name=j.name, register_number=j.register_number, proof=j.proof, subject=j.subject, test=j.test, purpose=j.purpose, type=j.type)
#        p.save()
#        filename = "YourPDF_Order.pdf"
#        p.pdf.save(filename, File(BytesIO()))
#    return HttpResponse(pdf, content_type='application/pdf')


#    for j in f:
#     context = {
#          'j': j,
#          'user':user,
#          'date':date
#     }
#    pdf = render_to_pdf('home/pdfformat.html', context)
     #pdf = render_to_pdf('your/pdf/template.html', context)
#    filename = "YourPDF_Order.pdf"
#    obj.pdf.save(filename, File(BytesIO(pdf.content)))
##


#def generate_pdfs_actual(request, pk=None, *args, **kwargs):
#    if pk:
#        user = User.objects.get(pk=pk)
#    else:
#        user = request.user
#    f = FinalPDFgeneratedstudents.objects.all()
#    date = ctime()
#    context = {
#         'f': f,
#         'user':user,
#         'date':date
#    }
#    for i in f:
#        pdf = render_to_pdf('home/pdfformat.html', context)
#    return HttpResponse(pdf, content_type='application/pdf')
