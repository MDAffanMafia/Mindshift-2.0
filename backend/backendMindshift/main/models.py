from django.db import models

# Create your models here.
class Post(models.Model):
    content=models.ImageField(upload_to="prodImages",default="shaikh3@gmail.com")