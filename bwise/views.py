from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import eventPost, picture, Otherpicture, BWSmembership, Article, Donation, Videos
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import NewBwsMemberForm, DonationForm, NewBwsMentorForm, NewBwsFellowForm, EventBusForm
from django.conf import settings
from django.db import IntegrityError



#Pdf options
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.

    
class MemberListView(ListView):
    model = BWSmembership
    template_name = 'invoice.html'
    ordering = ['-Date']
    # def get_queryset(self):
    #     return BWSmembership.objects.latest('id')

class DonorListView(ListView):
    model = Donation
    template_name = 'invoice_D.html'
 
    def get_queryset(self):
        return Donation.objects.latest('id')


def member_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    member = get_object_or_404(BWSmembership, pk=pk)

    template_path = 'pdf.html'
    context = {'member': member}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Invoice_membership.pdf'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def donor_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    don = get_object_or_404(Donation, pk=pk)

    template_path = 'pdfD.html'
    context = {'don': don}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Invoice_donation.pdf'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def index(request):

    event1 = eventPost.objects.all()
    pic = picture.objects.all()
    opic = Otherpicture.objects.all()
    article = Article.objects.all()
    video = Videos.objects.filter(id = 6) 

    return render(request, 'index.html', {'event1': event1, 'pic': pic, 'opic':opic, 'article':article, 'video':video })

def about(request):
    pic = picture.objects.all()
    return render(request, 'about.html', {'pic': pic})

def business(request):
    return render(request, 'business.html')

def writing(request):
    return render(request, 'writing.html')

def communication(request):
    return render(request, 'communication.html')

def stories(request):
    video = Videos.objects.all()
    return render(request, 'stories.html', {'video': video} )

def mentorship(request):

    form = NewBwsMentorForm()

    if request.method == 'POST':
        name = request.POST['Name']
        form = NewBwsMentorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            #messages.success(request, 'Account created successfully')
            return render(request, "mentorship.html", {'name': name})
        else:
            print('error form invalid')
    return render(request, 'mentorship.html', {'form': form})

def donation(request):

    form = DonationForm()

    if request.method == 'POST':

        form = DonationForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            #messages.success(request, 'Account created successfully')
            return successMsg1(request)

        else:
            print('error form invalid')

    return render(request, 'donation.html', {'form': form})

def fellowship(request):

    form = NewBwsFellowForm()

    if request.method == 'POST':
        name = request.POST['Name']
        form = NewBwsFellowForm(request.POST)
        if form.is_valid():
           form.save(commit=True)
            #messages.success(request, 'Account created successfully')
           return render(request, "fellowship.html", {'name': name})
        else:
            print('error form invalid')
    return render(request, 'fellowship.html', {'form': form})


def render_pdf_view(request):
    template_path = 'success1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def successMsg(request):

    return render(request, 'success1.html')

def successMsg1(request):

    return render(request, 'success.html')



def causes(request):
    return render(request, 'causes.html')

def membership(request):

    form = NewBwsMemberForm()

    if request.method == 'POST':
        name = request.POST['Name']
        form = NewBwsMemberForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            #messages.success(request, 'Account created successfully')
            return render(request, "membership.html", {'name': name})

        else:
            print('error form invalid')

    return render(request, 'membership.html', {'form': form})

def event(request):
    
    event1 = eventPost.objects.all()
    form = EventBusForm()

    if request.method == 'POST':
        name = request.POST['fullname']
        form = EventBusForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            #messages.success(request, 'Account created successfully')
            return render(request, "success1.html", { "name":name})
        else:
            print('error form invalid')
    
    return render(request, 'eventpost.html', {'event1': event1, 'form':form })


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
            ['info@bwisglobal.co.za'], # To Email
        )

        return render(request, "contact.html", {'name': name})

    else:
        return render(request, "contact.html", {})

        

def successView(request):
    return render(request, 'success.html')


