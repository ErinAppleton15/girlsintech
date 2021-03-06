from django.db import models
from django.utils import timezone
#from blog.models import Post
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    me = User.objects.get(username='admin')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
