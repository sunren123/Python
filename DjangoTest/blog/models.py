from django.db import models




class AreaInfo(models.Model):
    #地区名称
    atitle=models.CharField(max_length=20)
    #自关联属性

# Create your models here.
#一类
class BookInfo(models.Model):
    #图书名称
    btitle =models.CharField(max_length=20)
    # 日期
    bpub_date=models.DateField(auto_now=True)
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

    #指定模型类对应的表名称
    # class Meta:
    #     db_table ="HeroInfo"

# #新闻类
# class NewsType(models.Model):
#     #类型名称
#     type_name = models.CharField(max_length=20)
#     news_type = models.ManyToManyField("NewsInfo")
#
#
# #新闻详细类
# class NewsInfo(models.Model):
#     title = models.CharField(max_length=128)
#     pub_date = models.DateTimeField(auto_now_add=True)
#     content = models.TextField()


class AreaInfo(models.Model):
    #地区名称
    atitle = models.CharField(max_length=20)
    #关系属性，代表当前地区的腹肌地区
    aParent = models.ForeignKey('self', null=True, blank=True,on_delete=models.CASCADE)