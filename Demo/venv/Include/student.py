student_list = [{"name":"sunren","age":18,"stu_num":10000}]

def print_info():
    print("*"*20)
    print("欢迎来到学生管理系统")
    print("1.展示全部学生")
    print("2.搜索一个学生")
    print("3.增加一个学生")
    print("4.修改一个学生")
    print("5.删除一个学生")
    print("6.退出系统")
    print("*"*20)
    user_input=input("请选择序号：")
    return user_input

def show_all():
    for stu in  student_list:
        print(stu)

def search_stu():
    user_input_name = input("请输入学生的名字：")
    stu_exist =False
    for stu in student_list:
        if stu["name"] == user_input_name:
            stu_exist =True
            print(stu)
    if stu_exist ==False:
        print(">>>您要搜索的学生不存在")

def add_stu():
    stu_name =input("请添加学生姓名：")
    stu_age =input("请添加学生年龄：")
    stu_num =input("请添加学生学号：")
    new_stu= {"name":stu_name,"age":stu_age,"stu_num":stu_num}
    student_list.append(new_stu)
    print("学生：{}添加成功".format(stu_name))

def modify_stu_info():
    stu_name =input("请输入要修改的学生姓名：")
    stu_exist = False
    for stu in student_list:
        if stu["name"] == stu_name:
            stu_exist = True
            stu_age = input("请输入修改后的年:")
            stu_num = input("请输入修改后的学号:")
            stu["age"] = stu_age
            stu["stu_num"] = stu_num
            print("学生:{}信息更新成功".format(stu_name))
    if not stu_exist:
         print(">>>您要修改的学生不存在")

def delete_stu_info():
    stu_name =input("请输入要删除的学生姓名：")
    stu_exist = False
    for stu in student_list:
        if stu["name"] == stu_name:
            student_list.remove(stu)
            print("学生:{}信息删除成功".format(stu_name))
    if not stu_exist:
        print(">>>您要删除的学生不存在")


def main():
    while True:
        user_input = print_info()
        if user_input  in ["1","2","3","4","5","6"]:
            # print(user_input)
            if user_input == "1":
                show_all()
            elif user_input == "2":
                search_stu()
            elif user_input == "3":
                add_stu()
            elif user_input == "4":
                modify_stu_info()
            elif user_input == "5":
                delete_stu_info()
            elif user_input == "6":
                print(">>>再见")
                break

        else:
            print("不好意思，你输入错了，请重新输入")

main()
