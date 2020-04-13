#不可变对象实例
# def ChangeInt(a):
#     a = 10
#     print(a)
#
# b = 2
# ChangeInt(b)
# print(b)

#可变对象实例
# def changeme(mylist):
#     mylist.append([1,2,3,4])
#     print('函数内取值：',mylist)
#     return
#
# mylist = [10,20,30,40]
# changeme(mylist)
# print('函数外取值：',mylist)

#关键字参数
# def printme(str):
#     print(str)
#     return
# aa = 'cai'
# printme(str='菜鸟教程')
# printme(aa)

#不定长参数
# def printinfo(arg1,*vartuple):
#     print("输出：")
#     print(arg1)
#     print(vartuple)
#
# printinfo(70,80,90)
#
# def printinfo1(arg1,**vardict):
#     print('输出：')
#     print(arg1)
#     print(vardict)
#
# printinfo1(1, a=2,b=3)
#
# def printinfo2(a,b,*,c):
#     print(a+b+c)
#
# printinfo2(1,2,c=3)

#匿名函数
# sum1 = lambda arg1,arg2: arg1+arg2
# print(sum1(10,20))

#return语句
def sum1(a,b):
    total = a+b
    print('函数内：',total)
    return total

total = sum1(10,20)
print('函数外：',total)