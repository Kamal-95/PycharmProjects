# print("Hello")
#
# a = 3
# print(a)
#
# stri = "kamal"
# print(stri)
#
# b,c,d = 2,3.5,"rohini"
# print(b,c,d)
#
# print("value is =",b,c,d)
#
#
#
# print(type(b))
# print(type(c))
# print(type(d))
#
# print(stri + " " + d)
#
# value = [1,2.3,"Kamal",4,5]
#
# print(value[-1])
# print(value[-2])
# print(value[-3])
# print(value[1:3])
# value.insert(3,"Sharma")
# print(value)
# value.append("End")
# print(value)
# value[2] = "Rahul"
# print(value)
# del value[3]
# print(value)
#
# ####################################TUPLE##################
# #we can't Assigned again , its locked 1st time
# val =(1,2,"kamal",4.5)
# print(val)
# print(val[2])
#
# ###########DICTIONARY###########
#
# dic = {1:"kamal","b":2,"c":"cat",3:4}
# print(dic)
#
# print(dic[1])
# print(dic["b"])
# print(dic["c"])
# print(dic[3])
#
# dict = { }
#
# dict["firstname"] = "Kamal"
# dict["lastname"] = "Sharma"
# dict["age"] = 27
#
# print(dict)
#
# print(dict["firstname"])
#
# a=6
# if a>3:
#     print("True")
# else:
#     print("False")
# print("end of loop")


# obj = [2, 3, 4, 5, 6]
# for i in obj:
#     print(i*2)

# sum=0
# for i in range(1,6):
#     sum = sum + i
#     print(sum)

# for i in range(1,10,2):
#     print(i)

# for i in range(10):
#     print(i)
#
# it=4
# while it>1:
#     if it != 3:
#         print(it)
#     it = it -1

# it=4
# while it>1:
#     if it == 3:
#         print(it)
#         break
#     it = it -1
# it = 10
# while it>1:
#     if it == 9:
#         it = it-1
#         continue
#     if it == 3:
#         break
#     print(it)
#     it = it-1

# def GreetMe(name):
#     print("Good Morning "+name)
#
#
# def add(a,b):
#     return a+b
#
# print(add(2,3))
# GreetMe("Kamal")


# class Calculator:
#
#     def __init__(self):
#         self.a = "Calculator"
#
#     def Cal(self):
#         print(self.a)
#
#
# obj = Calculator()
#
# obj.Cal()


# class GeekforGeeks:
#
#     # default constructor
#     def __init__(self):
#         self.a = "GeekforGeeks"
#
#     # a method for printing data members
#     def print_Geek(self):
#         print(self.a)
#
#
# # creating object of the class
# obj = GeekforGeeks()
#
# # calling the instance method using the object obj
# obj.print_Geek()

# class Calculator:
#     num = 100
#     def __init__(self):
#         self.a = "Calculator"
#
#     def Cal(self):
#         print(self.a)
#
#     def getData(self):
#         print("funtion inside class")
#
#
# obj = Calculator()
# obj.getData()
# print(obj.num)
# obj.Cal()

class Calculator:
    num = 100  # class variable always constant

    def __init__(self, a, b):
        self.f1 = a  # instance variable1 always changing when new object is created
        self.s2 = b  # instance variable2 always changing when new object is created

    def Sum(self):
        return self.f1 + self.s2 + Calculator.num   #we can also use with class name as well. Calulator.num or self.num or obj.num



obj = Calculator(2,3)
print(obj.num)
print(obj.Sum())

obj = Calculator(4,5)
print(obj.num)
print(obj.Sum())





