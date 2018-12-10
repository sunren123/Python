from django.contrib import admin
from book import models
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','pub_date')#显示自己定义的名称
    list_editable = ("name","price")#可以编辑
    list_per_page = 10#分页
    search_fields = ("id","name","price",'pub_date')#添加搜索功能
    ordering = ("-price","id")

admin.site.register(models.Book,BookAdmin)
# admin.site.register(models.Book_Author)
admin.site.register(models.Publish)
admin.site.register(models.Author)