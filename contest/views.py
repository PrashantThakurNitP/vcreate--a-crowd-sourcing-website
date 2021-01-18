from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404

from django.contrib.auth import login,logout ,authenticate
#from django.contrib.auth.models import User
from contest.models import CustomUser #custom user
from django.db import IntegrityError
from django.contrib import messages
from .models import contestModel,submissionModel

from .forms import submissionForm,organisecontestForm,organiserdetailsForm

from django.contrib.auth.decorators import login_required
from datetime import datetime,date
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

def comp(request):
	#today_min = datetime.combine(date.today(), datetime.time.min)
	allcontest=contestModel.objects.all()
	return render(request, "contest/contest_home.html",{"allcontests":allcontest})
@login_required
def participated(request):
	#today_min = datetime.combine(date.today(), datetime.time.min)

	allcontest=contestModel.objects.filter(submissionmodel__submittedby=request.user)
	return render(request, "contest/contest_home.html",{"allcontests":allcontest})
@login_required
def organised(request):
	#today_min = datetime.combine(date.today(), datetime.time.min)
	if request.user.is_seller:
		allcontest=contestModel.objects.filter(organisedby=request.user)
		return render(request, "contest/contest_home.html",{"allcontests":allcontest})
	else:
		messages.success(request, 'You have not organised any contest ,You need to fill these detail for registering as contest organiser')
		return render(request, "contest/fill_seller_details.html",{'form':organiserdetailsForm()})

def livecontest(request):
	#today_min = datetime.combine(date.today(), datetime.time.min)
	allcontest=contestModel.objects.filter(enddate__gte =  date.today())
	return render(request, "contest/contest_home.html",{"allcontests":allcontest})
def pastcontest(request):
	#today_min = datetime.combine(date.today(), datetime.time.min)
	allcontest=contestModel.objects.filter(enddate__lt =  date.today())
	return render(request, "contest/contest_home.html",{"allcontests":allcontest})

	#return render(request, "contest/comp.html")
def checkallcontest(request):
	allcontest=contestModel.objects.all()
	return render(request, "contest/checkallcontest.html",{"allcontests":allcontest})
@login_required
def acceptsubmission(request):

	#allcontest=contestModel.objects.filter(organisedby=request.user)
	#return render(request, "contest/accept_submission.html",{"allsubmission":allcontest})
	if request.user.is_seller:
		allsubmission=submissionModel.objects.filter(contest__organisedby=request.user)

		return render(request, "contest/accept_submission.html",{"allsubmission":allsubmission})
	else:
		messages.success(request, 'You have not organised any contest ,You need to fill these detail for registering as contest organiser')
		return render(request, "contest/fill_seller_details.html",{'form':organiserdetailsForm()})

@login_required
def verifysubmission(request):

	#allcontest=contestModel.objects.filter(organisedby=request.user)
	#return render(request, "contest/accept_submission.html",{"allsubmission":allcontest})
	allsubmission=submissionModel.objects.filter(submittedby=request.user)

	return render(request, "contest/verify_submission.html",{"allsubmission":allsubmission})

def index(request):
	return render(request, "contest/index.html")
def logoutuser(request):

		if request.method=='POST' and request.user.is_authenticated:

				logout(request)
				return redirect('index')
				#return render(request,"posts/loginuser.html",{'form':AuthenticationForm()})
def logoutuser(request):

		if request.method=='POST' and request.user.is_authenticated:

				logout(request)
				return redirect('index')
def loginuser(request):
		if request.method== 'GET' :
                        print("GET METHOD")

                        return render(request,"contest/loginuser.html",{'form':AuthenticationForm()})

		elif request.method=='POST':
			user =authenticate(request,username=request.POST['username'], password=request.POST['password'])
			if user is None:
				messages.success(request, 'Account donot exist')

				return redirect("index")

									  #if user is none send them to same page with error
			else:
									  #login
				login(request,user)
				#messages.success(request, 'Welcome'+user.first_name)
				next=""
				if request.GET:

					next = request.GET['next']
				if next == "":
					return redirect('index')

				else:
					return redirect(next)
											#return HttpResponseRedirect(request.GET['next'])
											#return render(request,"posts/home.html",{"form":seeprofileForm()})

		else:
			messages.success(request, 'GET Method not allowed')

		return redirect("index")

def signupuser(request):
    if request.method== 'GET' :
                        print("GET METHOD")

                        return render(request,"contest/signupuser.html")
    elif request.method=="POST":


    		if request.POST['psw']==request.POST['psw-repeat']:
    			try:

    				user=CustomUser.objects.create_user( username=request.POST['email'], password=request.POST['psw'],email= request.POST['email'] )
    				name=request.POST['name']
    				user.first_name=name.split()[0]
    				user.last_name=name.split()[-1]

    				user.save()
    				return redirect("index")
    			except IntegrityError:
    				messages.success(request, 'Account with this email exist,choose another email or login')

    				return redirect("index")
    		else:
    				messages.success(request, 'Password donot match please try again')
    				return redirect("index")

    				#return render(request,"contest/index.html")




	#return render(request, "community/about.html")
def viewcontest(request,id1):
	if request.method =="GET": #when user first visit form show the form

				contest1=contestModel.objects.get(pk=id1)
				live=date.today()<=contest1.enddate
				return render(request,"contest/contest_detail.html",{'form':submissionForm(),"live":live,"contest":contest1})

@login_required
def organise(request):
	if request.user.is_seller:

			if request.method=="GET":
				return render(request, "contest/organise_contest.html",{'form':organisecontestForm()})

			elif request.method=="POST":

				form=organisecontestForm(request.POST,request.FILES)
				if form.is_valid():
					newcontest=form.save(commit=False)
					newcontest.organisedby=request.user
					newcontest.save()
					messages.success(request, 'contest organised with'+str(request.POST['title']))
					return render(request, "contest/index.html")
				else:
					messages.success(request, 'data not valid'+str(request.POST['title']))
					return render(request, "contest/index.html")
	else:
			if request.method=="GET":
				messages.success(request, 'You need to fill these detail for registering as contest organiser')
				return render(request, "contest/fill_seller_details.html",{'form':organiserdetailsForm()})

			elif request.method=="POST":
			        try:
        				user_object=CustomUser.objects.get(username=request.user.username)
        				if request.POST['bio']:
        					user_object.bio=request.POST['bio']
        				if request.POST['location']:
        					user_object.location=request.POST['location']
        				if request.POST['website']:
        					user_object.website=request.POST['website']
        				if request.FILES['image']:
        					user_object.image=request.FILES['image']
        				if request.POST['mobile']:
        					user_object.mobile=request.POST['mobile']
        				user_object.save()
        				messages.success(request, 'Thank you choosing us, we will verify your details and contact you ')
        				mail_subject = 'Request for oranising contest on vdesign'
        				message = render_to_string('contest/request_organise_contest_email.html',{'image': request.FILES['image'],'email' : request.user.email,'name': str(request.user.first_name)+" "+str(request.user.last_name),'bio': request.POST['bio'],'location': request.POST['location'],'mobile': request.POST['mobile'],'website': request.POST['website']})
        				to_email1='prashant09.thakur@gmail.com'

        				to_email3='anvesh.ashwin@gmail.com'
        				if request.user.email:
        				    to_email4=request.user.email
        				else:
        				    to_email4='prashantt.ug17.cs@nitp.ac.in'


        				email = EmailMessage(mail_subject, message, to=[to_email1,to_email3,to_email4])
        				email.send()
        				return render(request, "contest/index.html")
        			except:
        			    messages.success(request, 'All field required')
        			    return render(request, "contest/fill_seller_details.html",{'form':organiserdetailsForm()})





@login_required
def submit(request,contestid):
		if request.method =="GET": #when user first visit form show the form
				contest1=contestModel.objects.get(pk=contestid)
				return render(request,"contest/participate_contest.html",{'form':submissionForm(),"contest":contest1})

		elif request.method =="POST": #when user first visit form show the form





						contest1=contestModel.objects.get(pk=contestid)
						form=submissionForm(request.POST,request.FILES)

						newcontest=form.save(commit=False)
						#if request.user.is_authenticated:
							   #newtodo.user_new=request.user
							   #in newtodo user field is missing
						newcontest.submittedby=request.user
						newcontest.contest=contest1
						newcontest.save()
							#person2.save()
						messages.success(request,"your submission will be considered")
						return render(request, "contest/index.html")



