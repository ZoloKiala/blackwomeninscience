from django.contrib import admin
from .models import eventPost, picture, Otherpicture, membership

# Register your models here.

admin.site.register(eventPost)
admin.site.register(picture)
admin.site.register(Otherpicture)
admin.site.register(membership)