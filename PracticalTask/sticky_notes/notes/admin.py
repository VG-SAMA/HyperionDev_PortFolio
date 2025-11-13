from django.contrib import admin
from .models import Note

# Register your models here.
admin.site.register(Note)


"""
This registers the note Entity into the admin site to make changes directly.
"""
