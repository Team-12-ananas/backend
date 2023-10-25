from django.db import models


class Applicant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    welcome_text = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    relocation_status = models.BooleanField()
    professional_experience = models.TextField()
    education = models.TextField()
    about_me = models.TextField()
    photo = models.ImageField(upload_to='applicants/')
