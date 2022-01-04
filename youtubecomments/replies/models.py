from django.db import models


# Create your models here.
class Reply(models.Model):
    comment_id = models.ForeignKey('comments.Comment', on_delete=models.CASCADE)
    reply_content = models.CharField(max_length=500)