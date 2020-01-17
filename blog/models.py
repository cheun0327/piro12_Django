from django.db import models
from django.conf import settings

class Item(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(blank=True)   ## 둘다 문자열 저장
    ## 파이썬은 문자열은 하나인데 DB는 문자열에도 여러 종류있다.
    price = models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class  Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_url=models.URLField(blank=True)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True,
                            db_index=True)  # ModelAdmin.prepopulated_fields 편리 desc = models.TextField(blank=True) image = models.ImageField(blank=True)
# Pillow 설치가 필요 comment_count = models.PositiveIntegerField(default=0) tag_set = models.ManyToManyField('Tag', blank=True) is_publish = models.BooleanField(default=False) created_at = models.DateTimeField(auto_now_add=True) updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)