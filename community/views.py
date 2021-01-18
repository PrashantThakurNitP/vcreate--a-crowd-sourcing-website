from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404


def community(request):
	return render(request, "community/community.html")

def about(request):
	return render(request, "community/about.html")

