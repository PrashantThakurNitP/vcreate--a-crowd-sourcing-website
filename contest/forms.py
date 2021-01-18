from django.forms import ModelForm
from .models import submissionModel,contestModel
from django.contrib.auth.models import User
from contest.models import CustomUser

#this class is created so that to provide form for adding todo
#from phonenumber_field.formfields import PhoneNumberField
#class ClientForm(forms.Form):
from django import forms
class submissionForm(ModelForm):
    #specify what class and what model it would be working with
    class Meta:#specify what class we are working with
        model=submissionModel
        #mobile = PhoneNumberField()
        fields=['description','participant_email','document']#these are feature from model that we will set
        """
        widgets = {
            'participant_email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
            'description': forms.TextInput(attrs={'placeholder': 'Your description'}),
        """
class DateInput(forms.DateInput):
    input_type = 'date'
class organisecontestForm(ModelForm):
    #specify what class and what model it would be working with
    class Meta:#specify what class we are working with
        model=contestModel
        #mobile = PhoneNumberField()
        fields=['title','description','organiser_email','enddate','prize','guidlines','poster']#these are feature from model that we will set
        widgets = {
            'enddate': DateInput(),
        }

class organiserdetailsForm(ModelForm):
    #specify what class and what model it would be working with
    class Meta:#specify what class we are working with
        model=CustomUser
        #mobile = PhoneNumberField()
        fields=['bio','location','website','mobile','image']#these are feature from model that we will set
      

