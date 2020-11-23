from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.



class eventPost(models.Model):

    title = models.CharField(max_length = 200, unique = True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'pics')
    dateStart = models.DateTimeField()
    date1 = models.DateTimeField(auto_now_add = timezone.now)
    dateFinish = models.DateTimeField()
    address = models.CharField(max_length = 256)
    

    def __str__(self):
        return self.title
 
    def dateevent(self):
        return self.dateStart.strftime('%d %B')
    
    def dateeventS(self):
        return self.dateStart.strftime('%d %B %Y')

    def dateeventF(self):
        return self.dateFinish.strftime('%d %B %Y')

    def dateday(self):
        return int(self.date1.strftime("%d")) - int(self.dateStart.strftime("%d"))
    
    def datehour(self):
        return int(self.date1.strftime("%H")) - int(self.dateStart.strftime("%H"))

    def datemun(self):
        return int(self.date1.strftime("%M")) - int(self.dateStart.strftime("%M"))

    def dateyear(self):
        return int(self.date1.strftime("%Y")) - int(self.dateStart.strftime("%Y"))

    # def get_absolute_url(self):
    #     """Returns the url to access a particular author instance."""
    #     return reverse('eventpost-detail', args=[str(self.id)])

class picture(models.Model):

    about = models.ImageField(upload_to = 'pics')
    desc = models.TextField(default = True)


class Otherpicture(models.Model):

    header_bg = models.ImageField(upload_to = 'pics')
    logo = models.ImageField(upload_to = 'pics')
    about = models.ImageField(upload_to = 'pics')
    about_video = models.ImageField(upload_to = 'pics')

class Membership(models.Model):

    province_choices = (
        ('Eastern Cape', 'Eastern Cape'),
        ('Free State', 'Free State'),
        ('Gauteng', 'Gauteng'),
        ('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Limpopo', 'Limpopo'),
        ('Mpumalanga', 'Mpumalanga'),
        ('Northern Cape', 'Northern Cape'),
        ('Western Cape', 'Western Cape')
    )

    fullname = models.CharField(max_length = 200)
    email = models.EmailField(unique = True)
    province = models.CharField(max_length = 200, choices= province_choices)
    university =models.CharField(max_length = 200)

    def __str__(self):
        return self.fullname

class BWSmembership(models.Model):

    province_choices = (
        ('Eastern Cape', 'Eastern Cape'),
        ('Free State', 'Free State'),
        ('Gauteng', 'Gauteng'),
        ('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Limpopo', 'Limpopo'),
        ('Mpumalanga', 'Mpumalanga'),
        ('Northern Cape', 'Northern Cape'),
        ('Western Cape', 'Western Cape')
    )

    genre_choices = (
        ('male', 'male'),
        ('female', 'female'), 
    )
  
    age_choices = (
        ('18-24', '18-24'),
        ('25-29', '25-29'), 
         ('30-34', '30-34'),
        ('35-39', '35-39'), 
         ('40-49', '40-49'),
        ('49 and older', '49 and older'), 
    )

    race_choices = (
        ('african', 'african'),
        ('white', 'white'),
        ('indian', 'indian'),  
        ('color', 'color'),

    )

    town_choices = (
        ('Johannesburg', 'Johannesburg'),
        ('Durban', 'Durban'),
        ('indian', 'indian'),  
        ('Webinar', 'Webinar'),

    )
    qualification_choices = (
        ('Post PhD', 'Post PhD'),
        ('PhD', 'PhD'),
        ('Masters', 'Masters'),  
        ('Honours', 'Honours'),
        ('Bachelors', 'Bachelors'),
        ('Diploma', 'Diploma'),

    )

    occupation_choices = (
     
        ('Working', 'Working'),
        ('Working student', 'Working student'),
        ('Student', 'Student'),  

    )

    interested_choices = (
    
        ('yes', 'yes'),
        ('no', 'no'), 
    )

    timevolunteer_choices = (
        ('up to 2 hrs', 'up to 2 hrs'),
        ('up to 4 hrs', 'up to 4 hrs'), 
        ('up to 6 hrs', 'up to 6 hrs'),
        ('1 full day', '1 full day'),
    )


    Name = models.CharField(max_length = 200)
    Surname = models.CharField(max_length = 200)
    Gender = models.CharField(max_length = 200, choices= genre_choices)
    Cellphone = models.IntegerField()
    Email = models.EmailField(unique = True)
    Age = models.CharField(max_length = 200, choices= age_choices)
    Province = models.CharField(max_length = 200, choices= province_choices)
    University =models.CharField(max_length = 200)
    Race = models.CharField(max_length = 200, choices= race_choices)
    Country = models.CharField(max_length = 200)
    Town_attend_workshops = models.CharField(max_length = 200, choices = town_choices)
    Last_academic_qualification = models.CharField(max_length = 200, choices = qualification_choices)
    Current_academic_qualification = models.CharField(max_length = 200, choices = qualification_choices)
    Scientific_discipline = models.CharField(max_length = 200)
    Subject_major = models.CharField(max_length = 200)
    Occupation = models.CharField(max_length = 200)
    Where_hear_organisation = models.CharField(max_length = 200)
    Interested_mentorship_programs = models.CharField(max_length = 200,  choices = interested_choices)
    Time_to_volunteer = models.CharField(max_length = 200,  choices = timevolunteer_choices)
    Conducted_TV_interview = models.CharField(max_length = 200,  choices = interested_choices)
    Description = models.CharField(max_length = 400)
    Date = models.DateTimeField(auto_now_add = timezone.now)

    def __str__(self):
        return self.Name






   







  
        
 




    
    
   


   
    
    

    
    
