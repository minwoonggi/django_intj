from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article') # 작성자

    title = models.CharField(max_length=200, null=True) # 제목
    image = models.ImageField(upload_to='article/', null=False) # 이미지
    content = models.TextField(null=True) # 내용

    created_at = models.DateField(auto_now_add=True, null=True) # 작성일시

