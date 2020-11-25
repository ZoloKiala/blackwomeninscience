from django.contrib import admin
from .models import eventPost, picture, Otherpicture, Membership, BWSmembership, Article

# Register your models here.

admin.site.register(eventPost)
admin.site.register(picture)
admin.site.register(Otherpicture)
admin.site.register(Membership)
admin.site.register(BWSmembership)
admin.site.register(Article)