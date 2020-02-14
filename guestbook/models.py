from django.db import models
from oauth.models import User


# Create your models here.
class Message(models.Model):
    username = models.CharField('用户名', max_length=256)
    title = models.CharField('标题', max_length=512)
    content = models.TextField('留言内容', max_length=256)
    publish = models.DateTimeField('发表时间')

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name
        ordering = ['-publish']

    # 为了显示
    def __str__(self):
        return self.title
