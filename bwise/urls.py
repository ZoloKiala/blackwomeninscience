
from django.urls import path
#from .views import 
#EventListView, EventDetailView
from . import views
from .views import contactView, successView


urlpatterns = [
    path('', views.index, name = 'index'),
    path('charge', views.charge, name = 'charge'),
    path('success/', successView, name='success'),
    path('success/<str:args>/', views.successMsg, name = 'success'),
    path('about', views.about, name = 'about'),
    path('donation', views.donation, name = 'donation'),
    path('membership', views.membership, name = 'membership'),
    path('causes', views.causes, name = 'causes'),
    path('event', views.event, name = 'eventpost'),
    path('<int:pk>', views.event_detail, name='detail'),
    # path('event', EventListView.as_view(), name = 'eventpost'),
    # path('<int:pk>', EventDetailView.as_view(), name = 'eventpost-detail'),
    path('contact', contactView, name = 'contact'),

]
