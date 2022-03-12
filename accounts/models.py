from django.db import models
from django.contrib.auth.models import AbstractUser #add user to get back to old.
from django.db.models.signals import post_save
# Create your models here.
##remove it to get back to old
FA_CHOICES=[
    ('Rajasekaran', 'Rajasekaran'),
    ('Senthil Kumar', 'Senthil Kumar'),
    ("B. Sowmiya", "B. Sowmiya")
]
class User(AbstractUser):
 USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'faculty advisor'),
      (3, 'head of the department'),
      (4, 'admin'),
  )

 user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)
 facultyadvisor = models.CharField(max_length=100,  choices=FA_CHOICES, null=True)
 department = models.CharField(max_length=100, null=True)
 #
 image=models.ImageField(upload_to='profile_image', blank=True, null=True)
 #
##




class Students(models.Model):
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    ID_number=models.CharField(default='', max_length=100)
    Description=models.CharField(default='', max_length=100)
    phone=models.IntegerField(default=0)
    image=models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=Userprofile.objects.create(user=kwargs['instance'])

#post_save.connect(create_profile, sender=User)
