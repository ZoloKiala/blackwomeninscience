
from django.urls import path
#from .views import 
#EventListView, EventDetailView
from . import views
from .views import successView, render_pdf_view, MemberListView, member_render_pdf_view


urlpatterns = [
    path('', views.index, name = 'index'),
    path('success/', successView, name='success'),
    path('success/<str:args>/', views.successMsg, name = 'success'),
    path('invoice/', MemberListView.as_view(), name='member-list-view'),
    path('pdf/<pk>/', member_render_pdf_view, name='member-pdf-view'),
    path('about', views.about, name = 'about'),
    path('donation', views.donation, name = 'donation'),
    path('membership', views.membership, name = 'membership'),
    path('causes', views.causes, name = 'causes'),
    path('event', views.event, name = 'eventpost'),
    path('<int:pk>', views.event_detail, name='detail'),
    # path('event', EventListView.as_view(), name = 'eventpost'),
    # path('<int:pk>', EventDetailView.as_view(), name = 'eventpost-detail'),
    path('contact', views.contact, name = 'contact'),
]
