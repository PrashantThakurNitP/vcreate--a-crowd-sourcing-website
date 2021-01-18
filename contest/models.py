from django.db import models

# Create your models here.


from PIL import Image

from django.contrib.auth.models import User

#User._meta.get_field('email')._unique = True   for email to be unique
#from contest.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)
    is_seller=models.BooleanField(default=False,null=True)
    website=models.URLField(max_length=5000,blank=True,null=True)
    image=models.ImageField(upload_to='media/images/',blank=True,null=True)
    mobile = PhoneNumberField(blank=True,null=True)

class contestModel(models.Model):
	
	title=models.CharField(max_length=200,blank=True)
	organisedby=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	description=models.TextField(blank=True)
	organiser_email = models.EmailField(max_length=254,blank=True,null=True)
	enddate = models.DateField(blank=True,null=True)
	#about=models.TextField(blank=True,null=True)#it means having blank memeo is totally fine
	#created=models.DateTimeField(auto_now_add=True,blank=True,Default=False)#it means that it fixes time of its creation and it couldnot be changed
	#once it is set it cannot be changed
	prize=models.IntegerField(null=True)
	#image=models.ImageField(upload_to='media/images/',blank=True,null=True)
	poster=models.ImageField(upload_to='media/images/',blank=True,null=True)
	guidlines= models.FileField(upload_to='media/pdf/', max_length=1000000000, blank=True,null=True)
	"""
	def save(self):
		super().save()  
		print("path is ",self.poster.path)
	"""
	

	

	def __str__(self):
		#print("guidlines path",self.guidlines.path)
		return self.title


class submissionModel(models.Model):
	#name=models.ForeignKey(User,on_delete=models.CASCADE) #username

	contest=models.ForeignKey(contestModel,on_delete=models.CASCADE) #username
	submittedby=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	#title=models.CharField(max_length=200,blank=True)
	description=models.TextField(blank=True)
	participant_email = models.EmailField(max_length=254,blank=True,null=True)
	document= models.FileField(upload_to='media/pdf/', max_length=254, blank=True,null=True)

	

	def __str__(self):

		return str(self.contest)+" "+str(self.submittedby)




 #name=models.ForeignKey(User,on_delete=models.CASCADE) #username

 #title=models.ForeignKey(User,on_delete=models.CASCADE) #username