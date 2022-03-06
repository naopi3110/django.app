from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #djangoに元々入っているUser

#databaseの中の設定（入れるもの）
class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) #many to one(一人の著者が複数投稿可能) on_delete→Userが消えたら投稿も消去
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislike = models.BigIntegerField(default=0)

    def __str__(self):#あとでdjangoのアドミンで正しく表示させるためのコード
        return self.content[:30]#30文字まで表示



