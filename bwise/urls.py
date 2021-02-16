
from django.urls import path
#from .views import 
#EventListView, EventDetailView
from . import views
from .views import successView, render_pdf_view, MemberListView, member_render_pdf_view,donor_render_pdf_view, DonorListView


urlpatterns = [
    path('', views.index, name = 'index'),
    path('success/', successView, name='success'),
    path('success/<str:args>/', views.successMsg, name = 'success'),
    path('success1/<str:args>/', views.successMsg1, name = 'success1'),
    path('1nVo1ce/', MemberListView.as_view(), name='member-list-view'),
    path('invoiceD/', DonorListView.as_view(), name='donor-list-view'),
    path('pdf/<pk>/', member_render_pdf_view, name='member-pdf-view'),
    path('pdf1/<pk>/', donor_render_pdf_view, name='donor-pdf-view'),
    path('about', views.about, name = 'about'),
    path('donation', views.donation, name = 'donation'),
    path('fellowship', views.membership, name = 'membership'),
    path('membership', views.fellowship, name = 'fellowship'),
    path('causes', views.causes, name = 'causes'),
    path('business', views.business, name = 'business'),
    path('stories', views.stories, name = 'stories'),
    path('writing', views.writing, name = 'writing'),
    path('communication', views.communication, name = 'communication'),
    path('mentorship', views.mentorship, name = 'mentorship'),
    path('event', views.event, name = 'eventpost'),
    path('<int:pk>', views.event_detail, name='detail'),
    # path('event', EventListView.as_view(), name = 'eventpost'),
    # path('<int:pk>', EventDetailView.as_view(), name = 'eventpost-detail'),
    path('contact', views.contact, name = 'contact'),

]
