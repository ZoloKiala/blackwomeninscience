from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import eventPost, picture, Otherpicture
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import NewMemberForm
from django.conf import settings



# Create your views here.

def index(request):

    event1 = eventPost.objects.all()
    pic = picture.objects.all()
    opic = Otherpicture.objects.all()

    return render(request, 'index.html', {'event1': event1, 'pic': pic, 'opic':opic})

def about(request):
    pic = picture.objects.all()
    return render(request, 'about.html', {'pic': pic})

def donation(request):
    return render(request, 'donation.html')

def membership(request):

	form = NewMemberForm()

	if request.method == 'POST':

		form = NewMemberForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			#messages.success(request, 'Account created successfully')
			return successMsg(request)

		else:
			print('error form invalid')

	return render(request, 'membership.html', {'form': form})


def causes(request):
    return render(request, 'causes.html')

def event(request):
    
    event1 = eventPost.objects.all()
    
    return render(request, 'eventpost.html', {'event1': event1})


def event_detail(request, pk):
    
    event1 = get_object_or_404(eventPost, pk=pk)
    
    context= {'event1': event1,
              }
    
    return render(request, 'eventpost_detail.html', context)


def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']

        send_mail(
            subject, #subject
            message, #message
            email, # from email
            ['serkial1@yahoo.fr'], # To Email
        )

        return render(request, "contact.html", {'name': name})

    else:
        return render(request, "contact.html", {})

        

def successView(request):
    return render(request, 'success.html')


def successMsg(request):
	return render(request, 'success.html')



# class EventListView(ListView):
#     model = eventPost
#     template_name = 'eventpost.html'
#     context_object_name = 'event1'
#     ordering = ['date']

# class EventDetailView(DetailView):
#     context_object_name = 'event2'
#     model = eventPost
#     template_name = 'eventpost_detail.html'
    
