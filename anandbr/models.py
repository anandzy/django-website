from django.db import models

# Create your models here.


class Student (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

#The below tag will change the Boring display of the object to the firstname in admin page
    def __str__(self):
        return self.first_name



class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email
