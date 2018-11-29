from django.contrib import admin
from blog.models import PicTest
from blog.models import AreaInfo
# Register your models here.


class AreaStackedInline(admin.StackedInline):
    #多类的名称
    model = AreaInfo

class AreaInfoAdmin(admin.ModelAdmin):
    #地区管理类
    list_per_page = 50 #指定每页显示数据
    #列表模型属性
    list_display = ['id','atitle','title','parent']

    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['atitle'] #列表页右侧的过滤栏
    search_fields = ['atitle']#列表上搜索框

    fields = ['aParent','atitle']
    # fieldsets = (
    #     ('基本',{'filelds' : ['atitle']}),
    #     ('高级',{'filelds' : ['aParent']})
    #
    # )
    #嵌入方式
    inlines = [AreaStackedInline]

#添加到admin管理页面
admin.site.register(AreaInfo,AreaInfoAdmin)

admin.site.register(PicTest)
