from django.db import models

# Create your models here.



# Create your views here.


class Student(models.Model):
    name=models.CharField(max_length=100, null=False)
    email= models.EmailField(max_length=254 ,null=False)
    phone= models.CharField(max_length=10, null=False)

    def __str__(self):
          return self.name
