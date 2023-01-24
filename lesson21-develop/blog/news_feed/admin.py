from django.contrib import admin
from .models import Page, Post

# Register your models here.
admin.site.register(Page, Post)


