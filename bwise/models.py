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


   







  
        
 




    
    
   


   
    
    

    
    
