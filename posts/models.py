from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# Structured Query Language
# CREATE TABLE expenses (
#    id INTEGER PRIMARY_KEY AUTOINCREMENT,
#    name VARCHAR(100),
#)

class Post(models.Model):
    title = models.CharField(max_length=128) # Strings
    subtitle = models.CharField(max_length=128) # Strings
    body = models.TextField() # Large Sized String
    created_on = models.DateTimeField(auto_now_add=True) # Date and Time: MM / DD / YYYY HH:mm
    author = models.ForeignKey( # Creating a relation to another table
        User,
        on_delete=models.CASCADE
    )

    def __str__(self): # To String -> "Hello World by admin"
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        # Automatically redirect the user to an specific endpoint when a POST request is sent
        return reverse("post_detail", args=[self.id])