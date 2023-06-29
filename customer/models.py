from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 # support call, NPC, payment call    
    
BUSY = "Busy"
HELP = "Need_Help"
Call = "Support_Call"
NPC = "NPC _Call"
PAYMENT = "Payment_Call"

   
CALL_CHOICES = [
    (BUSY, "Busy"),
    (HELP, "Help"),
    (NPC, "NPC _Call"),
    (Call , "Support_Call"),
    (PAYMENT,"Payment_Call"),
    ]




class UserNote(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    text_note= models.TextField(max_length=500) 
    call_type = models.CharField(max_length=500,choices=CALL_CHOICES,default=BUSY)

    def __str__(self):
        return self.user.username



    


    

#     




        


    





    


    

    