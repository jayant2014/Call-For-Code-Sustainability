from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields as needed
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.email



from django.db import models

class SignUp(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)

    def __str__(self):
        return self.email


# models.py
from django.db import models
from django.contrib.auth.models import User

class CarbonCredit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credits = models.IntegerField(default=0)
    # Add more fields as needed, such as the date when credits were earned, source of credits, etc.


from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    # Add any additional fields you need
