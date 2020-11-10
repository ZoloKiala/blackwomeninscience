from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import eventPost, picture, Otherpicture
from django.shortcuts import render, get_object_or_404
from datetime import datetime
import stripe
from django.urls import reverse

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
    return render(request, 'membership.html')

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

def successMsg(request, args):
    amount = args
    return render(request, 'success.html', {'amount': amount})





# class EventListView(ListView):
#     model = eventPost
#     template_name = 'eventpost.html'
#     context_object_name = 'event1'
#     ordering = ['date']

# class EventDetailView(DetailView):
#     context_object_name = 'event2'
#     model = eventPost
#     template_name = 'eventpost_detail.html'
    
    
    







def contact(request):
    return render(request, 'contact.html')