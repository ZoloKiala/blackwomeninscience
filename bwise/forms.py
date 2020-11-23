from django import forms

from  bwise.models import Membership, BWSmembership

class NewMemberForm(forms.ModelForm):

    class Meta():

        model = Membership
        fields = ('fullname', 'email', 'province', 'university')

        widgets = {

        'fullname' : forms.TextInput(attrs = {'class': "form-control"}),
        'email' : forms.TextInput(attrs = {'class': "form-control"}),
        'province' : forms.Select(attrs = {'class': "form-control"}),
        'university' : forms.TextInput(attrs = {'class': "form-control"})
        }

class NewBwsMemberForm(forms.ModelForm):

    class Meta():

        model = BWSmembership
        exclude = ['Date']

        widgets = {
            'Name' : forms.TextInput(attrs = {'class': "form-control"}),
            'Email' : forms.TextInput(attrs = {'class': "form-control"}),
            'Surname' : forms.TextInput(attrs = {'class': "form-control"}),
            'Gender' : forms.Select(choices= BWSmembership.genre_choices, attrs = {'class': "form-control"}),
            'Description' : forms.Textarea(attrs = {'class': "form-control"}),
            'Town_attend_workshops' : forms.TextInput( attrs = {'class': "form-control"}),


        }



  
