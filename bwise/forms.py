from django import forms

from  bwise.models import BWSmembership, Donation, BWSmentorship, BWSfellowship, EventBus



class NewBwsMemberForm(forms.ModelForm):

    Name = forms.CharField(label="What is your name", widget=forms.TextInput(attrs={'class':'form-control'}))

    Surname = forms.CharField(label="What is your surname", widget=forms.TextInput(attrs={'class':'form-control'}))

    genre_choices = [
        ('male', 'Male'),
        ('female', 'Female'), 
      ]

    Gender = forms.ChoiceField(choices=genre_choices, widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))

    Cellphone = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))

    Email = forms.EmailField( 
        label="Please enter your email address", widget=forms.TextInput(attrs={'class':'form-control'}))

    age_choices = [
        ('18-24', '18-24'),
        ('25-29', '25-29'), 
         ('30-34', '30-34'),
        ('35-39', '35-39'), 
         ('40-49', '40-49'),
        ('49 and older', '49 and older'), 
        
    ]

    Age = forms.ChoiceField(choices=age_choices, widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))

    province_choices = [
        ('Eastern Cape', 'Eastern Cape'),
        ('Free State', 'Free State'),
        ('Gauteng', 'Gauteng'),
        ('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Limpopo', 'Limpopo'),
        ('Mpumalanga', 'Mpumalanga'),
        ('Northern Cape', 'Northern Cape'),
        ('Western Cape', 'Western Cape')
    ]

    Province = forms.ChoiceField(choices=province_choices, widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))
    
    University = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    race_choices = [
        ('african', 'African'),
        ('white', 'White'),
        ('indian', 'Indian'),  
        ('color', 'Color'),

    ]

    Race = forms.ChoiceField(choices= race_choices, widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))

    Country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    
    town_choices = (
        ('Johannesburg', 'Johannesburg'),
        ('Durban', 'Durban'),

    )

    Town_attend_workshops = forms.ChoiceField(label="Select preferred town to attend BWIS Workshops/ Activities", choices= town_choices,
    widget=forms.HiddenInput(), required=False)

    qualification_choices = (
        ('Post PhD', 'Post PhD'),
        ('PhD', 'PhD'),
        ('Masters', 'Masters'),  
        ('Honours', 'Honours'),
        ('Bachelors', 'Bachelors'),
        ('Diploma', 'Diploma'),

    )

    Last_academic_qualification = forms.ChoiceField(label="Last obtained academic qualification", choices= qualification_choices,
    widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))

    Current_academic_qualification = forms.ChoiceField(label="Current Academic studies", choices= qualification_choices,
    widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))

    Scientific_discipline = forms.CharField(label="What is your scientific discipline ?", widget=forms.TextInput(attrs={'class':'form-control'}))

    Subject_major = forms.CharField(label="What is your subject major ?", widget=forms.TextInput(attrs={'class':'form-control'}))

    occupation_choices = [
     
        ('Working', 'Working'),
        ('Working student', 'Working student'),
        ('Student', 'Student'),  

    ]

    Occupation = forms.ChoiceField(label="What is your occupation ?", choices= occupation_choices,
    widget=forms.Select(attrs={'class':'form-control narrow-select'}))

    hear_choices = (
        ('social media', 'Social media'),
        ('radio', 'Radio'), 
        ('friend', 'Friend'),
        ('colleague', 'Colleague'),
        ('university', 'University'),
    )

    Where_hear_organisation = forms.ChoiceField(label="Where did you hear about our organisation ?", choices= hear_choices,
    widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'})) 

    interested_choices = [
    
        ('yes', 'Yes'),
        ('no', 'No'), 
    ]

    Interested_mentorship_programs = forms.ChoiceField(label="Are you interested in mentorship programs ?", choices= interested_choices,
    widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'})) 

    timevolunteer_choices = (
        ('up to 2 hrs', 'up to 2 hrs'),
        ('up to 4 hrs', 'up to 4 hrs'), 
        ('up to 6 hrs', 'up to 6 hrs'),
        ('1 full day', '1 full day'),
    )

    Time_to_volunteer = forms.ChoiceField(label="How much time can you volunteer in BWIS activities ?", choices= timevolunteer_choices,
    widget=forms.Select(attrs={'style': 'padding-left:10px', 'class':'form-control', 'class': 'narrow-select'})) 


    interested_choices = (
    
        ('yes', 'Yes'),
        ('no', 'No'), 
    )

    Conducted_TV_interview = forms.ChoiceField(label="Have you conducted Radio/TV interview ?", choices= interested_choices,
    widget=forms.Select(attrs={'style': 'width:100px', 'class':'form-control narrow-select'})) 

    media_handle = forms.CharField(label="Please share your social media handle (s) ?",

    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. Linkdeln, Facebook, Instagram & Twitter'}))

    Description = forms.CharField(label="Please provide a brief description of yourself ?",
    max_length = 400,
    widget=forms.Textarea(attrs={'rows':5, 'class':'form-control'}))

    
    class Meta():

        model = BWSmembership
        exclude = ['Date']
        error_css_class = "error"

        # widgets = {
        #     'Name' : forms.TextInput(attrs = {'class': "form-control"}),
        #     'Email' : forms.TextInput(attrs = {'class': "form-control"}),
        #     'Surname' : forms.TextInput(attrs = {'class': "form-control"}),
        #     'Gender' : forms.Select(choices= BWSmembership.genre_choices, attrs = {'class': "form-control"}),
        #     'Description' : forms.Textarea(attrs = {'class': "form-control"}),
        #     'Town_attend_workshops' : forms.TextInput( attrs = {'class': "form-control"}),

class NewBwsFellowForm(forms.ModelForm):

    Name = forms.CharField(label="What is your name ?", widget=forms.TextInput(attrs={'class':'form-control'}))

    Surname = forms.CharField(label="What is your surname ?", widget=forms.TextInput(attrs={'class':'form-control'}))

    genre_choices = [
        ('male', 'Male'),
        ('female', 'Female'), 
      ]

    Gender = forms.ChoiceField(choices=genre_choices, widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))

    Cellphone = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))

    Email = forms.EmailField( 
        label="Please enter your email address", widget=forms.TextInput(attrs={'class':'form-control'}))

    age_choices = [
        ('18-24', '18-24'),
        ('25-29', '25-29'), 
         ('30-34', '30-34'),
        ('35-39', '35-39'), 
         ('40-49', '40-49'),
        ('49 and older', '49 and older'), 
        
    ]

    Age = forms.ChoiceField(choices=age_choices, widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))

    province_choices = [
        ('Eastern Cape', 'Eastern Cape'),
        ('Free State', 'Free State'),
        ('Gauteng', 'Gauteng'),
        ('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Limpopo', 'Limpopo'),
        ('Mpumalanga', 'Mpumalanga'),
        ('Northern Cape', 'Northern Cape'),
        ('Western Cape', 'Western Cape'),
        ('Other', 'Other')
    ]

    Province = forms.ChoiceField(choices=province_choices, widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))
    
    University = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    race_choices = [
        ('african', 'African'),
        ('white', 'White'),
        ('indian', 'Indian'),  
        ('color', 'Color'),

    ]

    Race = forms.ChoiceField(choices= race_choices, widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))

    Country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


    qualification_choices = (
        ('Post PhD', 'Post PhD'),
        ('PhD', 'PhD'),
        ('Masters', 'Masters'),  
        ('Honours', 'Honours'),
        ('Bachelors', 'Bachelors'),
        ('Diploma', 'Diploma'),

    )

    Last_academic_qualification = forms.ChoiceField(label="Last obtained academic qualification", choices= qualification_choices,
    widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))

    Current_academic_qualification = forms.ChoiceField(label="Current Academic studies", choices= qualification_choices,
    widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))

    Scientific_discipline = forms.CharField(label="What is your scientific discipline ?", widget=forms.TextInput(attrs={'class':'form-control'}))

    Subject_major = forms.CharField(label="What is your subject major ?",  widget=forms.TextInput(attrs={'class':'form-control'}))

    occupation_choices = [
     
        ('Working', 'Working'),
        ('Working student', 'Working student'),
        ('Student', 'Student'),  

    ]

    Occupation = forms.ChoiceField(label="What is your occupation ?", choices= occupation_choices,
    widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))

    hear_choices = (
        ('social media', 'Social media'),
        ('radio', 'Radio'), 
        ('friend', 'Friend'),
        ('colleague', 'Colleague'),
        ('university', 'University'),
    )

    Where_hear_organisation = forms.ChoiceField(label="Where did you hear about our organisation ?", choices= hear_choices,
    widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'})) 

    interested_choices = [
    
        ('yes', 'Yes'),
        ('no', 'No'), 
    ]

    Conducted_TV_interview = forms.ChoiceField(label="Have you conducted Radio/TV interview ?", choices= interested_choices,
    widget=forms.Select(attrs={'style': 'width:100px', 'class':'form-control narrow-select'})) 

    media_handle = forms.CharField(label="Please share your social media handle (s)",

    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. Linkdeln, Facebook, Instagram & Twitter'}))

    Description = forms.CharField(label="Please provide a brief description of yourselfS",
    max_length = 400,
    widget=forms.Textarea(attrs={'rows':5, 'class':'form-control'}))

    
    class Meta():

        model = BWSfellowship
        exclude = ['Date']
        error_css_class = "error"



class DonationForm(forms.ModelForm):

    Name = forms.CharField(label="What is your name ?", widget=forms.TextInput(attrs={'class':'form-control'}))

    Surname = forms.CharField(label="What is your surname ?", widget=forms.TextInput(attrs={'class':'form-control'}))

    Reason_donation = (
        ('Fundraising', 'Fundraising'),
        ('Mentorship program', 'Mentorship program'),

    )

    Cellphone = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))

    Email = forms.EmailField( 
        label="Please enter your email address", widget=forms.TextInput(attrs={'class':'form-control'}))

    Amount_donation = forms.IntegerField(label="Enter Amount to donate (Rand)",
    widget=forms.TextInput(attrs={'class':'form-control narrow-select'}))

    Reason_donation = forms.ChoiceField(label="Select the reason for donation", choices= Reason_donation,
    widget=forms.Select(attrs={'style': 'width:100px', 'class':'form-control narrow-select'}))

    class Meta():

        model = Donation
        exclude = ['Date']
        error_css_class = "error"

class NewBwsMentorForm(forms.ModelForm):

    Name = forms.CharField(label="What is your name ?", widget=forms.TextInput(attrs={'class':'form-control'}))

    Surname = forms.CharField(label="What is your surname ?", widget=forms.TextInput(attrs={'class':'form-control'}))

    Cellphone = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))

    Email = forms.EmailField( 
        label="Please enter your email address", widget=forms.TextInput(attrs={'class':'form-control'}))

    age_choices = [
        ('18-24', '18-24'),
        ('25-29', '25-29'), 
         ('30-34', '30-34'),
        ('35-39', '35-39'), 
         ('40-49', '40-49'),
        ('49 and older', '49 and older'), 
        
    ]

    Age = forms.ChoiceField(choices=age_choices, widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))

    province_choices = [
        ('Eastern Cape', 'Eastern Cape'),
        ('Free State', 'Free State'),
        ('Gauteng', 'Gauteng'),
        ('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Limpopo', 'Limpopo'),
        ('Mpumalanga', 'Mpumalanga'),
        ('Northern Cape', 'Northern Cape'),
        ('Western Cape', 'Western Cape')
    ]

    Province = forms.ChoiceField(choices=province_choices, widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))
    
    Country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    qualification_choices = (
        ('Post PhD', 'Post PhD'),
        ('PhD', 'PhD'),
        ('Masters', 'Masters'),  
        ('Honours', 'Honours'),
        ('Bachelors', 'Bachelors'),
        ('Diploma', 'Diploma'),

    )

    Last_academic_qualification = forms.ChoiceField(label="Last obtained academic qualification", choices= qualification_choices,
    widget=forms.Select(attrs={'class':'form-control', 'class': 'narrow-select'}))

    Scientific_discipline = forms.CharField(label="What is your scientific discipline ?", widget=forms.TextInput(attrs={'class':'form-control'}))
 
    Share_experience = forms.CharField(label="Share your own experience of being mentored for relatability",
    max_length = 400,
    widget=forms.Textarea(attrs={'rows':5, 'class':'form-control'}))

    Description_idea = forms.CharField(label="Describe your ideal mentee ( stipulate any prerequisites of your ideal mentee)",
    max_length = 400,
    widget=forms.Textarea(attrs={'rows':5, 'class':'form-control'}))

    timementor_choices = [
        ('2-5 hours', '2-5 hours'),
        ('5-10 hours', '5-10 hours'), 
        ('10-15 hours', '10-15 hours'),
        ('more than 15 hours', 'more than 15 hours'),
    ]
    Time_to_mentorship = forms.ChoiceField(label="How much time can you dedicate to the mentorship program in a week ?", choices= timementor_choices,
    widget=forms.Select(attrs={'style': 'padding-left:10px', 'class':'form-control', 'class': 'narrow-select'})) 

    class Meta():

        model = BWSmentorship
        exclude = ['Date']
        error_css_class = "error"

        # widgets = {
        #     'Name' : forms.TextInput(attrs = {'class': "form-control"}),
        #     'Email' : forms.TextInput(attrs = {'class': "form-control"}),
        #     'Surname' : forms.TextInput(attrs = {'class': "form-control"}),
        #     'Gender' : forms.Select(choices= BWSmembership.genre_choices, attrs = {'class': "form-control"}),
        #     'Description' : forms.Textarea(attrs = {'class': "form-control"}),
        #     'Town_attend_workshops' : forms.TextInput( attrs = {'class': "form-control"}),



class EventBusForm(forms.ModelForm):

    fullname = forms.CharField(label="What is your name ?", widget=forms.TextInput(attrs={'class':'form-control'}))

    cellphone = forms.IntegerField(label="Your cellphone number ?", widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField( 
        label="Please enter your email address", widget=forms.TextInput(attrs={'class':'form-control'}))

    scientific_d = forms.CharField(label="What is your scientific discipline ?", widget=forms.TextInput(attrs={'class':'form-control'}))

    interested_choices1 = (
    
        ('yes', 'yes'),
        ('no', 'no'), 
    )
    notifications = forms.ChoiceField(label="Would you like to receive notifications from BWIS on future events ?", 
                    choices = interested_choices1, widget=forms.Select(attrs={'style': 'width:100px', 'class':'form-control narrow-select'}))

    class Meta():

        model = EventBus
        exclude = ['date']
        error_css_class = "error"


