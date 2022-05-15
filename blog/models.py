from django.db import models

# Create your models here.
class Post(models.Model):
    타이틀 = models.CharField(max_length = 50)
    내용 = models.TextField()
    작성일 = models.DateTimeField(auto_now_add = True)
    업데이트 = models.DateTimeField(auto_now = True)


    def __str__(self):
        return  f'[{self.pk}]{self.타이틀}'


    