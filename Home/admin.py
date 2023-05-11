from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(AboutPage)
admin.site.register(ContactForm)
class QuillPostAdmin(admin.ModelAdmin):
    pass