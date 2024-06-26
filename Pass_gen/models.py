from django.db import models

class Password(models.Model):
    """A password that user creates"""    
    password = models.CharField(max_length=30)
    password_length = models.PositiveIntegerField()
    
    def __str__(self):
        """returns a string representation of the model"""
        return self.password

