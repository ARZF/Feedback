from django.db import models

class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")
