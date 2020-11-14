from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import eventPost, picture, Otherpicture
from django.shortcuts import render, get_object_or_404
from datetime import datetime
import stripe
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from bwise.forms import NewMemberForm, ContactForm
from django.conf import settings


### Strip key
stripe.api_key = "sk_test_51Hhtf5BoSJcXeEmytgYmoSEjdMBtNzn8jIpG9bTqaLDSbSkJmRDTsDb8JNZnJXcTPbX8SithLc35iVhFCpPPpRS500evxnmrXS"


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




def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['serkial1@yahoo.fr'], fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'success1.html')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return render(request, 'success.html')

def charge(request):


	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='usd',
			description="Donation"
			)

	return redirect(reverse('success', args=[amount]))



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
    
