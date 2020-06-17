from django.db import models
from django.contrib.auth.models import User

class Demo(models.Model):

    img = models.ImageField(upload_to='pics')
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    

    
  
