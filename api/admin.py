from django.contrib import admin

from api.models import Student

# Register your models here.
from .models import Student

admin.site.register(Student)
