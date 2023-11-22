from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank.png')
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    file = models.FileField(upload_to='post_files/%y')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user
    
class LikedPost(models.Model):
    post_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
        
class FollowersCount(models.Model):
    
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.user
    


class Defaultdisplay(models.Model):
    name = models.CharField(max_length=1000)
    file = models.FileField(upload_to='default_posts')
    by = models.CharField(max_length=100)

    def __str__(self):
        return self.name



