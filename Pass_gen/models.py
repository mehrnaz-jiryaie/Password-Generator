from django.db import models
# from validator import UnsignedNonZeroIntegerField

class Password(models.Model):
    # A password that user creates
    password_length = models.PositiveIntegerField()
    
    # def __str__(self):
    #     # returns password
    #     return self.password
