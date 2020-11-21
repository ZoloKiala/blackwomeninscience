from django import forms

from  bwise.models import membership

class NewMemberForm(forms.ModelForm):

    class Meta():

        model = membership
        fields = ('fullname', 'email', 'province', 'university')

        widgets = {

        'fullname' : forms.TextInput(attrs = {'class': "form-control"}),
        'email' : forms.TextInput(attrs = {'class': "form-control"}),
        'province' : forms.Select(attrs = {'class': "form-control"}),
        'university' : forms.TextInput(attrs = {'class': "form-control"})
        }



  
