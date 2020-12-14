from django.contrib import admin
from .models import eventPost, picture, Otherpicture, BWSmembership, Article, Donation, BWSmentorship, Videos

# Register your models here.

admin.site.register(eventPost)
admin.site.register(picture)
admin.site.register(Otherpicture)
# admin.site.register(Membership)
admin.site.register(BWSmembership)
admin.site.register(BWSmentorship)
# admin.site.register(Article)
admin.site.register(Donation)
admin.site.register(Videos)