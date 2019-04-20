from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200,blank=True, null=True, unique=True, default=None)
    dept = models.CharField(max_length=20,default=None)
    message = models.CharField(max_length=20,default=None)



    def __str__(self):
         return self.email
