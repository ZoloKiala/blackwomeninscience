from django.db import models
from datetime import datetime
from django.utils import timezone
import datetime
from datetime import date

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length = 200, unique = True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'pics')
    date = models.DateTimeField(auto_now_add = timezone.now)

class Videos(models.Model):

    name = models.CharField(max_length = 200, unique = True)
    # description = models.TextField(default=True)
    video = models.FileField(upload_to = 'videos/')

    def __str__(self):
        return self.name

    

class eventPost(models.Model):

    title = models.CharField(max_length = 200, unique = True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'pics')
    dateStart = models.DateTimeField()
    date1 = models.DateTimeField(auto_now_add = timezone.now)
    dateFinish = models.DateTimeField()
    address = models.CharField(max_length = 256)
    last_used = models.DateTimeField(default=datetime.datetime.now().date(), editable=False)

    @property
    def days_since_use(self):
        return (self.last_used.date() - datetime.datetime.now().date()).days
    

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

    def dateday1(self):
        d = self.dateStart - self.last_used
        return d.days
    
    def datehour1(self):
        hourleft = int(self.dateStart.strftime("%H"))  - int(datetime.datetime.now().hour)
        return hourleft

    def datemun1(self):
        munleft = int(self.dateStart.strftime("%M")) - int(datetime.datetime.now().minute)
        return munleft

    
    def datehour(self):
        return int(self.date1.strftime("%H")) - int(self.dateStart.strftime("%H"))

    def datemun(self):
        return int(self.date1.strftime("%M")) - int(self.dateStart.strftime("%M"))

    def dateyear(self):
        return int(self.date1.strftime("%Y")) - int(self.dateStart.strftime("%Y"))



class picture(models.Model):

    about = models.ImageField(upload_to = 'pics')
    desc = models.TextField(default = True)


class Otherpicture(models.Model):

    header_bg = models.ImageField(upload_to = 'pics')
    logo = models.ImageField(upload_to = 'pics')
    about = models.ImageField(upload_to = 'pics')
    about_video = models.ImageField(upload_to = 'pics')

class Donation(models.Model):

    Reason_donation = (
        ('Fundraising', 'Fundraising'),
        ('Mentorship program', 'Mentorship program'),

    )

    Name = models.CharField(max_length = 200)
    Surname = models.CharField(max_length = 200)
    Organization = models.CharField(max_length = 200)
    Cellphone = models.IntegerField()
    Email = models.EmailField(unique = True)
    Reason_donation =  models.CharField(max_length = 200, choices= Reason_donation)
    Amount_donation =  models.IntegerField()
    Date = models.DateTimeField(auto_now_add = timezone.now)

    def __str__(self):
        return self.Name




class BWSfellowship(models.Model):

    province_choices = (
        ('Eastern Cape', 'Eastern Cape'),
        ('Free State', 'Free State'),
        ('Gauteng', 'Gauteng'),
        ('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Limpopo', 'Limpopo'),
        ('Mpumalanga', 'Mpumalanga'),
        ('Northern Cape', 'Northern Cape'),
        ('Western Cape', 'Western Cape'),
        ('Other', 'Other')
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
        ('None', 'None'),

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

    hear_choices = (
        ('social media', 'Social media'),
        ('radio', 'Radio'), 
        ('friend', 'Friend'),
        ('colleague', 'Colleague'),
        ('university', 'University'),
    )


    Name = models.CharField(max_length = 200)
    Surname = models.CharField(max_length = 200)
    Gender = models.CharField(max_length = 200, choices= genre_choices)
    Cellphone = models.IntegerField()
    Email = models.EmailField(unique = True)
    Age = models.CharField(max_length = 200, choices= age_choices)
    University =models.CharField(max_length = 200)
    Race = models.CharField(max_length = 200, choices= race_choices)
    City = models.CharField(max_length = 200)
    Province = models.CharField(max_length = 200, choices= province_choices)
    Country = models.CharField(max_length = 200)
    Last_academic_qualification = models.CharField(max_length = 200, choices = qualification_choices)
    Current_academic_qualification = models.CharField(max_length = 200, choices = qualification_choices)
    Scientific_discipline = models.CharField(max_length = 200)
    Subject_major = models.CharField(max_length = 200)
    Occupation = models.CharField(max_length = 200, choices = occupation_choices)
    Where_hear_organisation = models.CharField(max_length = 200, choices = hear_choices)
    Conducted_TV_interview = models.CharField(max_length = 200,  choices = interested_choices)
    media_handle = models.CharField(max_length = 200, default=True)
    Description = models.CharField(max_length = 400)
    Date = models.DateTimeField(auto_now_add = timezone.now)
    


    def __str__(self):
        return self.Name

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
        ('None', 'None'),

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

    hear_choices = (
        ('social media', 'Social media'),
        ('radio', 'Radio'), 
        ('friend', 'Friend'),
        ('colleague', 'Colleague'),
        ('university', 'University'),
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
    Occupation = models.CharField(max_length = 200, choices = occupation_choices)
    Where_hear_organisation = models.CharField(max_length = 200, choices = hear_choices)
    Interested_mentorship_programs = models.CharField(max_length = 200,  choices = interested_choices)
    Time_to_volunteer = models.CharField(max_length = 200,  choices = timevolunteer_choices)
    Conducted_TV_interview = models.CharField(max_length = 200,  choices = interested_choices)
    media_handle = models.CharField(max_length = 200, default=True)
    Description = models.CharField(max_length = 400)
    Date = models.DateTimeField(auto_now_add = timezone.now)
    


    def __str__(self):
        return self.Name
# class Membership(models.Model):

#     province_choices = (
#         ('Eastern Cape', 'Eastern Cape'),
#         ('Free State', 'Free State'),
#         ('Gauteng', 'Gauteng'),
#         ('KwaZulu-Natal', 'KwaZulu-Natal'),
#         ('Limpopo', 'Limpopo'),
#         ('Mpumalanga', 'Mpumalanga'),
#         ('Northern Cape', 'Northern Cape'),
#         ('Western Cape', 'Western Cape')
#     )

#     fullname = models.CharField(max_length = 200)
#     email = models.EmailField(unique = True)
#     province = models.CharField(max_length = 200, choices= province_choices)
#     university =models.CharField(max_length = 200)

#     def __str__(self):
#         return self.fullname

        

class BWSmentorship(models.Model):

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

    qualification_choices = (
        ('Post PhD', 'Post PhD'),
        ('PhD', 'PhD'),
        ('Masters', 'Masters'),  
        ('Honours', 'Honours'),
        ('Bachelors', 'Bachelors'),
        ('Diploma', 'Diploma'),

    )


    timementor_choices = [
        ('2-5 hours', '2-5 hours'),
        ('5-10 hours', '5-10 hours'), 
        ('10-15 hours', '10-15 hours'),
        ('more than 15 hours', 'more than 15 hours'),
    ]


    Name = models.CharField(max_length = 200)
    Surname = models.CharField(max_length = 200)
    Cellphone = models.IntegerField()
    Email = models.EmailField(unique = True)
    Age = models.CharField(max_length = 200, choices= age_choices)
    Province = models.CharField(max_length = 200, choices= province_choices)
    Country = models.CharField(max_length = 200)
    Scientific_discipline = models.CharField(max_length = 200)
    Last_academic_qualification = models.CharField(max_length = 200, choices = qualification_choices)
    Share_experience = models.CharField(max_length = 400)
    Description_idea = models.CharField(max_length = 400)
    Time_to_mentorship = models.CharField(max_length = 200,  choices = timementor_choices)
    Date = models.DateTimeField(auto_now_add = timezone.now)

    def __str__(self):
        return self.Name




   







  
        
 




    
    
   


   
    
    

    
    
