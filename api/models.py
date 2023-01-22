from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=25, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]
    
    
    
    
    # auto_now means everytime we save a note it will take a time 
    # stamp of when that noted was saved or upated. 
    
    # auto_now_add only takes a time stamp on creates. 


