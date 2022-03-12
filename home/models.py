from django.db import models
#from django.contrib.auth.models import AbstractUser  #import User to get back to previous way.
from accounts.models import User, Students  ##uncomment to get back to old
##this is of least importance.
#class Post(models.Model):
    #post = models.CharField(max_length=100)
    #user = models.ForeignKey(User)
    #created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now=True)
##can be removed.


##
#class FacultyAdvisor(model.Model):

##


class Student(models.Model):
    users = models.ManyToManyField(User)   #
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def make_student(cls, current_user, new_student):
        student, created=cls.objects.get_or_create(
            current_user=current_user
        )
        student.users.add(new_student)


    @classmethod
    def loose_student(cls, current_user, new_student):
        student, created=cls.objects.get_or_create(
            current_user=current_user
        )
        student.users.remove(new_student)

#class FacultyAdvisor(models.Model):
#    users = models.OneToOneField(User)
#    users.user_type=2

class Bonafied(models.Model):
    proof = models.FileField(upload_to = "students/bonafied")
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100, null=True)
    purpose = models.CharField(max_length=200, null=True)
    Fa_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


##
INTERNSHIP_CHOICES=[
    ('On Campus', 'On Campus'),
    ('Off Campus', 'Off Campus')
]
class Internship(models.Model):
    proof = models.FileField(upload_to = "students/Internship")
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, choices=INTERNSHIP_CHOICES, null=True)
    Fa_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
##


##
TEST_CHOICES = [
    ('CT1', 'CT1'),
    ('CT2', 'CT2'),
    ('CT3', 'CT3'),
]

SUBJECT_CHOICES = [
    ('OS', 'OS'),
    ('CD', 'CD'),
    ('DS', 'DS'),
    ('DSD', 'DSD'),
]

class Retest(models.Model):
    proof = models.FileField(upload_to = "students/Retest")
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100, null=True)
    #test = models.CharField(max_length=50, null=True)
    #subject = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES, null= True)
    test = models.CharField(max_length=100, choices=TEST_CHOICES, null= True)
    Fa_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
##





##
class Accepted_students(models.Model):
    proof = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True, blank=True)

    subject = models.CharField(max_length=100, null= True, blank=True)
    test = models.CharField(max_length=100, null= True, blank=True)
    purpose = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        unique_together = ["proof", "register_number", "type", "subject", "test", "purpose"]

    def __str__(self):
        return self.name
##




class FinalPDFgeneratedstudents(models.Model):
    proof = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True, blank=True)

    subject = models.CharField(max_length=100, null= True, blank=True)
    test = models.CharField(max_length=100, null= True, blank=True)
    purpose = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        unique_together = ["proof", "name", "register_number", "type", "subject", "test", "purpose"]

    def __str__(self):
        return self.name






class YourModel(models.Model):
       proof = models.CharField(max_length=100, null=True)
       name = models.CharField(max_length=100, null=True)
       register_number = models.CharField(max_length=100, null=True)
       type = models.CharField(max_length=100, null=True, blank=True)

       subject = models.CharField(max_length=100, null= True, blank=True)
       test = models.CharField(max_length=100, null= True, blank=True)
       purpose = models.CharField(max_length=200, null=True, blank=True)
       pdf = models.FileField(upload_to='stuents/pdfs', null=True, blank=True)
       def __str__(self):
           return self.name
