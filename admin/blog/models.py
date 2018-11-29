from django.db import models


# Create your models here.

class AreaInfo(models.Model):
    # 地址模型
    atitle = models.CharField(verbose_name="标题", max_length=20)
    # 自关联属性
    aParent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle

    # 列表排序
    title.admin_order_field = "id"
    # 指定显示名称
    title.short_description = "地区名称"

    def parent(self):
        if self.aParent is None:
            return ''
        return self.aParent.atitle

    parent.short_description = "父级名称"


class PicTest(models.Model):
    # 上传图片
    goods_pic = models.ImageField(upload_to='blogtest')

