from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass # Store past searches, maybe check for accuracy later?

#Store most popular searches/number of times a location has been queried 
