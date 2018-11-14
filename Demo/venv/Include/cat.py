class Cat:

    def __init__(self,name,color):
        print("cat正在实例化")
        self.cat_name =name
        self.cat_color =color


    def eat(self):
        print("我的{}在吃饭！！".format(self.cat_name))# self 指的是实例


    def drinl(self):
        print("我的{}在喝可乐!!".format(self.cat_name))

    def play(self):
        print("到处跑")

# if __name__ == "__main__":
#     my_cat =Cat("大黄","黄色")
#     my_cat.eat()
#     my_cat.drinl()
#     my_cat.play()

tom =Cat()
print(tom.name)