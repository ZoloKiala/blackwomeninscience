
from django.urls import path
from . import views
#from .views import successView, render_pdf_view, MemberListView, member_render_pdf_view,donor_render_pdf_view, DonorListView


urlpatterns = [
   path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
