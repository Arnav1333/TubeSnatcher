from django.contrib.auth.models import User
from django.db import models

class Download(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    video_title = models.CharField(max_length=255)
    download_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.video_title} downloaded by {self.user.username} on {self.download_date}"
