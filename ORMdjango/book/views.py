from django.db.models import Avg, Sum,Q,F
from django.shortcuts import render,redirect

# Create your views here.
from book.models import Book,Publish,Author,Book_Author
def index(request):
    book = Book.objects.all()
    # pub_obj = Publish.objects.filter(name="武汉晨报")[0]
    #
    # print(pub_obj.book_set.all().values("name", "price"))

    #     ret = Book.objects.filter(publish__name="武汉晨报").values("name", "price")
    # print(ret)
    #
    # ret1 = Publish.objects.filter(book__name="java").values("name")
    # print(ret1)

    # book_obj = Book.objects.get(id=1)
    # author_objs = Author.objects.all()
    # book_obj.authors.add(*author_objs)
    # # book_obj.authors.remove(1)

    # Book_Author.objects.create(book_id=1,author_id=2)
    # obj= Book.objects.get(id=1)
    # obj.book_author_set.all()[0].author
    # ret=Book.objects.filter(book_author__author__name="sunren").values("name","price")
    # print(ret)
    # ret = Book.objects.all().aggregate(Avg("price"))
    # ret1 = Book.objects.all().aggregate(Sum("price"))
    # print(ret1)
    # print(ret)
    Book.objects.all().update(price=F("price")+10)

    return render(request, "index.html" , locals())


def addbook(request):
    #第一种方式
    #Book.objects.create(name="python",price=99,author="yuan",pub_date="2018-12-12")
    #第二中方式
    book = Book(name="python",price=99,author="yuan",pub_date="2018-12-12")
    book.save()
    return redirect("/index")



def delete(request):
    # 删除点击的图书
    # book = Book.objects.get(id=bid)
    book = Book.objects.filter(name="python")
    book.delete()
    return redirect("/index")


def update(request):

    return redirect("/index")