from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # 1:1
    # related_name이 'profile'이면 request.user.profile.nickname 이렇게 바로 접근 가능
    image = models.ImageField(upload_to='profile/', null=True) # MEDIA_ROOT 아래 profile에 저장
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
