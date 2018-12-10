

from django.db import models



class Book(models.Model):

    name = models.CharField(max_length=20,verbose_name="书名")
    price = models.IntegerField(verbose_name="价格")
    pub_date = models.DateTimeField()
    publish = models.ForeignKey("Publish",on_delete=models.CASCADE)



class Book_Author(models.Model):
    book = models.ForeignKey("Book",on_delete=models.CASCADE)
    author = models.ForeignKey("Author",on_delete=models.CASCADE)


class Publish(models.Model):

    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)


class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=20,default=20)



class Classes(models.Model):
    #班级表
    title = models.CharField(max_length=20)
    m =models.ManyToManyField("Teachers")
class Teachers(models.Model):
    #老师表
    name = models.CharField(max_length=20)



class Student(models.Model):
    username = models.CharField(max_length=20)
    age = models.IntegerField(max_length=20)
    gender = models.BooleanField()
    cs = models.ForeignKey(Classes,on_delete=models.CASCADE)