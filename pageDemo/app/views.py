from django.shortcuts import render,HttpResponse,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


USER_LIST = []
for i in range(1,666):
    temp = {'name':'root'+str(i), 'age':i}
    USER_LIST.append(temp)

def index(request):
    per_page_count = 10
    current_page = request.GET.get('p')
    current_page = int(current_page)
    # p=1
    # 0,10   0-9
    # p=2
    # 10,20   10-19
    start = (current_page-1) * per_page_count
    end = current_page*per_page_count
    data = USER_LIST[start:end]

    if current_page<=1:
        prev_pager = 1
    prev_pager = current_page -1
    next_pager = current_page +1
    return render(request,'index.html',{'user_list':data,'prev_pager':prev_pager,'next_pager':next_pager})

class CustomPaginator(Paginator):
    def __init__(self,current_page, per_pager_num,*args,**kwargs):
        # 当前页
        self.current_page = int(current_page)
        # 最多显示的页码数量 11
        self.per_pager_num = int(per_pager_num)
        super(CustomPaginator,self).__init__(*args,**kwargs)
    def pager_num_range(self):
        # 当前页
        #self.current_page
        # 最多显示的页码数量 11
        #self.per_pager_num
        # 总页数
        # self.num_pages
        if self.num_pages < self.per_pager_num:
            return range(1,self.num_pages+1)
        # 总页数特别多 5
        part = int(self.per_pager_num/2)
        if self.current_page <= part:
            return range(1,self.per_pager_num+1)
        if (self.current_page + part) > self.num_pages:
            return range(self.num_pages-self.per_pager_num+1,self.num_pages+1)
        return range(self.current_page-part,self.current_page+part+1)


def index1(request):

    # 全部数据：USER_LIST，=》得出共有多少条数据
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象（是否具有下一页；是否有上一页；）
    current_page = request.GET.get('p')
    # Paginator对象
    paginator = CustomPaginator(current_page,7,USER_LIST, 10)
    try:
        # Page对象
        posts = paginator.page(current_page)
        # has_next              是否有下一页
        # next_page_number      下一页页码
        # has_previous          是否有上一页
        # previous_page_number  上一页页码
        # object_list           分页之后的数据列表，已经切片好的数据
        # number                当前页
        # paginator             paginator对象
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,'index1.html',{'posts':posts})


from django import forms
from django.forms import fields

class F1Form(forms.Form):
    #required 默认不为空
    user = fields.CharField(max_length=18,
                            min_length=6,
                            required=True,
                            error_messages={
                                "required":"用户名不能为空",
                                "max_length": "用户名太长了",
                                "min_length": "用户名太短了",
                            }
                            )

    pwd = fields.CharField(required=True,min_length=6,
                           error_messages={
                               "required": "密码不能为空",
                               "min_length": "密码太短了",
                           }
                           )

    age = fields.IntegerField(required=True)
    email = fields.EmailField(required=True,min_length=8,
                              error_messages={
                                  "required": "邮箱不能为空",
                                  "min_length": "密码太短了",
                                  "invalid":"邮箱格式错误"
                              }
                              )
    city = fields.ChoiceField(
        choices= [(1,"上海"),(2,"广州")],
        initial=1  #默认选择
    )
    bobby = fields.MultipleChoiceField(
        choices=[(1, "刚良"), (2, "附件"), (3, "你的")],
    )


















def f1(request):

    if request.method == "GET":
        obj =F1Form()
        return render(request,"f1.html",locals())
    else:
        # u=request.POST.get('user')
        # p=request.POST.get('pwd')
        # a=request.POST.get('age')
        # e=request.POST.get('email')
        # print(u,p,a,e)

        obj = F1Form(request.POST)
        if obj.is_valid():
            print("验证成功",obj.cleaned_data)
            return redirect("https://gitee.com")
        else:
            print("验证失败",obj.errors)
        return render(request,'f1.html',{"obj":obj})
