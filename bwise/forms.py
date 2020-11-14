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


class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.TextInput(attrs = {'class': "form-control"}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs = {'class': "form-control"}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs = {'class': "form-control"}), required=True)

  
