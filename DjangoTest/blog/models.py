from django.db import models

# Create your models here.
#一类
class BookInfo(models.Model):
    #图书名称
    btitle =models.CharField(max_length=20)
    # 日期
    bpub_date=models.DateField()
    # 阅读量
    bread =models.IntegerField(default=0)
    # 评论
    bcomment= models.IntegerField(default=0)
    # 是否删除
    isDelete=models.BooleanField(default=False)

#多类
class HeroInfo(models.Model):
    #英雄名称
    hname= models.CharField(max_length=20)
    #英雄性别
    hgender =models.BooleanField(default=False)
    #备注
    hcomment= models.CharField(max_length=200)
    #关系属性
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE,)
    # 是否删除
    isDelete = models.BooleanField(default=False)

