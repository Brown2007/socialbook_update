from django.contrib import admin
from .models import Profile, Post, LikedPost, FollowersCount, Defaultdisplay
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikedPost)
admin.site.register(FollowersCount)
admin.site.register(Defaultdisplay)
