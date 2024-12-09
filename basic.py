
#thislist = ["apple", "banaba", "cherry", "orange", "kiwi"]
# for i in range(len(thislist)):
#     print(i , thislist[i])
 
#     print(thislist)

#thislist.insert(2, "blackcarrant")
#thislist.insert(5 , "waterlemon")
#print(thislist)
# thistuple = ("aa" , "bb")
# thislist.extend(thistuple)
# print(thistuple)

# thislist.clear()
# print(thislist)
# newlist = [y for y in thislist if "e" in y]
# print(newlist)
# num = [1,2,3,4,5,6,7,8,9,10]
# newnum = [x ** 2 for x in num ]
# print(newnum)
# newnum = ["odd" if i % 2 != 0 else "even" for i in num]
# print(newnum)
# number = [44, 53, 65, 78, 82, 87, 93, 96, 98, 99]
# oddnum = []
# evennum = []
# for i in number:
#    if i % 2 != 0:
#     oddnum.append(i)
#    else:
#     evennum.append(i)
# print("oddnum =", oddnum)
# print("evennum =", evennum)
# matrix = [[1,2,3], [4,5,6],[7,8,9]]
# index1 = 0
# for i in matrix:
#     index2 = 0
#     for j in i:
#         if j ==1 or j ==5 or j ==9:
#             print ("valu is", j)
#             print(f"index position[{index1}][{index2}]")
#         index2 += 1
#     index1 += 1        

#num = [9, -1, 5, 10, 3, 1, -7, 100]
# num.sort()
# print(num) 
# sorted_number = sorted(num) #permanent
# print(sorted_number)
# num.sort(reverse=True)
# print(num)
# thislist = ["a", "b", "c"]
# #mylist = thislist #copy to both
# mylist = thislist.copy() #copy to new one only
# thislist.append("d")
# print(mylist)
# print(thislist)
#tuple
# tup = (1,2,3,4,5)
# mylist = list(tup)
# m = [6,7,8,9]
# mylist.extend(m) #append ma bataa add hunchh tar extend ma list ma bhako number matra add hunchh
# tup1= tuple(mylist)
# print(tup1)


# sum =0
# matrix = [[1,2,3], [4,5,6], [6,7,8],[9,10,11]]
# for x in matrix:
#     for y in x:
#         sum = sum + y
# print(sum)
#result =0
#result += sum()

# st = {"aa", "bb", "cc"}
# pxrint(st)
#thisset = {"aa", "bb", "c"}
# thisset.add("dd")
# print(thisset)
# tropical = {"ee", "ff", "gg"}
# thisset.update(tropical)
# print(thisset)
# thisset.remove("2")
# print(thisset)
# thisset.discard("2")
# print(thisset)
# set1 = {"a", "b", "c"}
# # set2 = {1,2,3}
# # set3 = set1.union(set2) 
# # print(set3)
# set4 = {2, 5, 7, "a", "d"}
# # 
# set6 = set1 & set4
# print(set6)
# sum=0
# lst1 = []
#lst = [(1,2), (2,3), (3,4), (1,0), (1,1)]
# for x in lst:
#     sumnumber = sum(x)
#     if sumnumber != 0:
#         sum1 = sumnumber
#         if sumnumber > sum1:
#             print(sumnumber)
# result = []
# #result [[(1,2,3),6]]
# for x in lst: #(1,2,3) (4,3,4)
#     if not result:
#         sum_numbers = sum(x)
#         result.append([x,sum_numbers])
# else:
#     sum_numbers =sum(x)
#     if result[0][1] < sum_numbers:
#         result.clear()
#         result.append([x, sum_numbers])
#     print(result)
# matrix = [(1,2,3), (4,9,8), (9,4,3)]
# result = []
# for i in matrix:
#     if not result:
#         sum_number = sum(i)
#         result.append([i, sum_number])
#     else:
#         sum_number = sum(i)
#         if result[0][1]<sum_number:
#             result.clear()
#             result.append([i,sum_number])
#         print(result)
# s = "Hello, World"
# print(s.replace("World", "Python"))
# a = 10
# b = 20
# temp = a
# a = b
# b = temp 
# print(a,b)

# for x in range(6): 
#     print(x)
# for x in range(2,6): 
#     print(x)
# for x in range(2,12,1): 
#     print(x)
# list = []
# list1 = []
# for x in range(2,10): 
#     if x % 2 != 0:
#      list.append(x)
#     else:
#      list1.append(x)
# print("odd:",list)
# print("even:",list1)

#s = "hello, world"
#print(s[-2])
# print(s[2:5])
# print(s[7:])
# print(s[::2])
#print(s[::-1]) revesre
#print(len(s))
# for i in range(len(s)):
#     print(f"character at index {i} is {s[i]}")
# list = []
# count = 0
# for i in range(len(s)):
#     if s[i] == "a" or s[i] =="e" or s[i] =="i" or s[i] =="o" or s[i] =="u":
#         list.append(s[i])
#         count = count+1
# print("vowel:",list, "no of vowel:", count)
# for w in s:
#     if w == "h":
#         print("h character")
#     else:
#         print(f"the character is {w} not h")
# array = []
# for i in s:
#     if i == "a" or i =="e" or i =="i" or i =="o" or i=="u":
#         array.append(i)
# print(array, len(array))
# s = "Hello"
# s = "h" + s[0:]
# print(s)
#s= "aaaaaaaaaaaaaaaaahellobbbbbbbbb"
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.lstrip('a'))
# print(s.rstrip('b'))
#print(s.strip('ab'))
# matrix = [(1,2,3), (4,9,8), (9,4,3)]
# result = []
# for i in matrix:
#     if not result:
#         sum_number = sum(i)
#         result.append([i, sum_number])
#     else:
#         sum_number = sum(i)
#         if result[0][1]<sum_number:
#             result.clear()
#             result.append([i,sum_number])
# print(result)

# var  = [[(4, 9, 8), 21, 22]] # 0 bhitro 2nd element 1 ho = var[0][1]=21, var[0][2]=22
# xyz = var[0] = [(4, 9, 8), 21]
# xyz[1]
# var[0][1]
# lst = [1,2,3,4,1,2,3,4,5,6]
# lst1= set(lst)
# print(lst1)
# my_dict = {
# "name": "ram",
# "age": 30,
# "city": "kat"
# }
# print(my_dict["name"])
# print(my_dict.get("adress", "adress not found"))
# my_dict["hometown"] = "BIRGUNJ"
# my_dict["name"] = "shyam"
# print(my_dict)
# del my_dict["age"]
# for key in my_dict:
#   # print(key, ':', my_dict[key])
#   print(key)
#   print(my_dict[key])

#     if my_dict[key] == 30:
#         print(key,my_dict[key])

# my_dict = {"name": "ram",
# "age": 30,
# "city": "kat",
# "grade":{
#     "math": 90,
#     "history": 54,
#     "science": 67},
# "contact": {
#     "email": "ict.dhm@gmail.com",
#     "phone": "9845854701"
# }}
# print(my_dict["grade"]["math"])
# print(my_dict["contact"]["phone"])
# print(my_dict.get("contact").get("phone"))
# print(my_dict.get("contact").get("adress"))
# print(my_dict.get("homeadress").get("phone"))
# my_dict["grade"]["literature"] = 90
# my_dict["contact"]["telephone"] = 909090909
# print(my_dict)
# for x in my_dict.keys():
#     print(x)
# for x in my_dict.values():
#     print(x)
# for x, y in my_dict.items():
#     print(x,y)
# for k, v in my_dict.items():
#     # if type (v) == dict:
#     print(f"key: {k}, value: {type(v)}")  

# grade = {
#     "math": 90,
#     "history": 54,
#     "science": 67}
# s = "hello, world"
# print(s.split())
# s2 = " "
# s1 = ["hello", "world", "nepal"]
# print(s2.join(s1))
# print(s.split(","))
# print(" ".join(s1))
# s= "12345"
# print(s.isdigit())
# # s = "hello"
# print(s.islower())
# a=5
# b=10
# s= f"the sum of {a} and {b} is {a+b}"
# print(s)
#s= "i am the \"bacher\" student"
# s= 'i am the "bacher" student'
# print(s)
# for i, j in my_dict.items():
#     if type(j) == dict:
#         print(f"key = {i} , value ={type(j)}")

# def addition(x,y): 
#     result = x+y
#     print("sum is", result) # not working without return

# sum1 = addition(1,9)
# print("sum1",sum1)

# 
# def substraction(x,y):
#     result = x-y
#     print("subtract is", result)
#     return result

# substract1 = substraction(115,6)
# print("substract1",substract1)
# substract2 = substraction(200,9)
# print("substract2",substract2)
# lst = [1,2,3,4,5]
# substract1 = substraction(lst)

# def addition(x):
#     print("x",x)
#     sum_value = sum(x)
#     max_value = max(x)
#     min_value = min(x)
#     return sum_value, max_value, min_value
# lst = [1,2,3,4,5]
# result = addition(lst)
# print(result)
# print("sum", result[0])

# def addition(a, b=10):
#     sum10 = a+b
#     subtrac10 = a-b
#     return sum10, subtrac10

# result1 = addition(5)  
# print(result1)
# result1 = addition(5, 15)  
# print(result1)

# def addition(a,b):
#     sum2 = a+b
#     return sum2

# def substract(x,y):
#     subs2 = x-y
#     return subs2

# def multiply(p,q):
#     mul2 = p-q
#     return mul2

# def division(r,s):
#     div2 = r-s
#     return div2

# print("1.addition\n")
# print("2.substraction\n") 
# print("3.multiply\n")
# print("4.division\n")               
# option = int (input ("enter the option"))
# if option == 1:
#     value1 = int (input("enter the first number"))
#     value2 = int (input("enter the second number"))
#     result = addition(value1, value2)
#     print("the sum is", result)
# if option == 2:
#     value1 = int (input("enter the first number"))
#     value2 = int (input("enter the second number"))
#     result = substract(value1, value2)
#     print("the substract is", result)

# if option == 3:
#     value1 = int (input("enter the first number"))
#     value2 = int (input("enter the second number"))
#     result = substract(value1, value2)
#     print("the multiply is", result)  

# if option == 4:
#     value1 = int (input("enter the first number"))
#     value2 = int (input("enter the second number"))
#     result = division(value1, value2)
#     print("the division is", result)

# a= int(input("ENTER THE ROLLNO"))
# def student_result( arg2, arg3, arg4, arg5):
#     if a == 1:
#      student = {
#         1:{
#                 "name": arg2,
#                 "marks":{
#                         "math": arg3,
#                         "science": arg4,
#                         "english": arg5
#                 } }}
#     totalmarks = student[1]["marks"]["math"] + student[1]["marks"]["science"] + student[1]["marks"]["english"] 
#     return student[1]["name"], totalmarks
    
# result = student_result("ram", 40, 30, 38)
# print(result)
# x = int(input("enter the student"))   
# def marksofstudent(a):
#         student = { 
#         1:{
#                 "name":"ram",
#                 "marks":{
#                         "math": 30,
#                         "science": 40,
#                         "englist": 50
#                 },
#         },
#         2:{
#                 "name":"shyam",
#                 "marks":{
#                         "math": 40,
#                         "science": 40,
#                         "englist": 50
#                 }
#         },
#         3:{
#                 "name":"hari",
#                 "marks":{
#                         "math": 30,
#                         "science": 60,
#                         "englist": 50
#                 }
#         }   }
#         identity = student[a]["name"]
#         overallmarks = student[a]["marks"]["math"] + student[a]["marks"]["science"] +student[a]["marks"]["englist"]
#         return identity, overallmarks

# id,

# total_marks = marksofstudent(x)
# print(id)
# print(total_marks)

# y = 20
# def my_function():
#         print("inside function:", y)

# my_function()
# print("outside function:", y)  
# def my_function(*kids): 
#         print("the y")     
# def my_function():
#         x=10
#         print("inside function:",x)
# list = []
# sum = 0
# def add(*args): 
#        print("args", type(args)) 
#        list.extend(args)
#        sum = list[1] + list[2]
#        return sum
       

# r1 = add(1,2,3,4,5,6,7)   
# print(r1)     

# def my_function(**kid):
#         print(type(kid))
#         print("his last name is" + kid["lname"])

# my_function(fname = "tobias", lname = "refsnem")        
# def student(*a, **b):
#         print("name", b)



# student(20,20 20, fname = "shyam", lname = "kumar")




#FIBNACCI SERIES
# x = 10
# def add():
#         global x
#         x = x + 10
#         print("inside",x)

# add()
# print("outside",x)        
# 


# 


# def fib(n):
#         if n <= 1:
#                 return 1
#         else:
#                 return (fib(n-1) + fib(n-2))
        
# for i in range(10):
#         print(fib(i))
# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "watermelon")
# print(thislist)
# a1 = ["apple", "banana", "cherry"]
# a2 = ("mango", "pineapple", "papaya")
# a1.extend(a2)
# print(a1)
#thisTUPLE = ["apple", "banana", "cherry"]
# newlist = []
# for x in thislist:
#     if 'a' in x:
#         newlist.append(x)
# print(newlist)
# newlist = []
# for x in thislist:
#     if x != "banana":
#         newlist.append(x)
#     else:
#         x = "orange"
#         newlist.append(x)
#     print(newlist)

# thislist.sort()
# print(thislist)
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.clear()
# print(thislist)

# thistupil = ("apple", "banana", "cherry")
# y = list(thistupil)
# for i in y:
#     if i != "banana":
#         y.append(i)
#     else:
#         i = "orange"
#         y.append(i)
#     z = tuple(y)   
  #  print(z)     
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)
# def fib(n):
#         if n <= 1:
#                 return 1
#         else:
#                 return (fib(n-1) + fib(n-2))
        
# for i in range(10):
#         print(fib(i))
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)
# thisdict = {
#   "a": "Ford",
#   "b": "Mustang",
#   "c": 1964
# }

# x = thisdict.keys()

# print(x)
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"
# car["base"] = 4000

# print(x) #after the change
# substraction = lambda a : a - 12
# print(substraction(20))

# def addition (x): #same as lambda
#   x = x + 10
#   return x
# print(addition(15))

# mul = lambda a, b, c : a*b*c
# print(mul(4,5,8))
 
# div = lambda a, b : a/b
# print(div(30,5))
# list ma sabai data eutai type ko bhyo bhane array ho like all integer value
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def greet(self):
#     return f"Hello. my name is {self.name} and I am {self.age} years old"

# person1 = Person("Alice", 40)
# person2 = Person("ram",45)
# print(person1.name)
# print(person2.name)
# print(person2.age)

# message = person1.greet()
# print(message)
# class Car:
#   wheels = 4
#   def __init__(self, make, model):
#     self.make = make
#     self.model = model

#   def review(self):
#     return f"this {self.make} {self.model} is most selling type"
  
# Car1 = Car("rts", 2020)
# print(Car1.model)
# a = Car1.review()
# print(a)
# print(Car.wheels)
# print(Car1.wheels)
# class Area:
#   pi = 3.14
#   def rectangle (self, length, breath):
#     return length*breath
#   def square (self, length):
#     return length*length
#   def circle (self, radius):
#     return self.pi * (radius **2)

# area1 = Area()
# print("AREA of rectangle", area1.rectangle(2,3))
# print("AREA of square", area1.square(6))
# print("AREA of circle", area1.circle(6))
# perimeter nikalne
# c
# class perimeter:
#   pi = 3.14
#   def rectangle(a, l, b):
#     return 2*(l+b)
#   def square(b, l):
#     return 4*l
#   def circle(c, r):
#     return 2*c.pi*r

# p1 = perimeter()
# print("perimeter of rectangle:", p1.rectangle(6,8))
# print("perimeter of square:", p1.square(5))
# print("perimeter of circle:", p1.circle(3))

# class Animal:
#   def speak(self):
#     return "animal speaks"
# class Dog(Animal):
#   def bark(self):
#     return "Dog barks"
# print(Animal().speak())
# print(Dog().speak())
# print(Dog().bark())
# my_dog = Dog()
# print(my_dog.speak())

# class A:
#   def method_A(self):
#     return "method A"
# class B:
#   def method_b(self):
#     return "method B"
# class C(A,B):
#   def method_c(self):
#     return "method C"
# obj_c = C()
# print(obj_c.method_A())
# print(obj_c.method_B())
# print(obj_c.method_C())

# class A:
#   def method_A(self):
#     return "method A"
# class B(A):
#   def method_B(self):
#     return "method B"
# class C(B):
#   def method_C(self):
#     return "method C"

# obj_c = C()
# print(obj_c.method_A())
# print(obj_c.method_B())
# print(obj_c.method_C())


# class rectangle:
#   def __init__(self, length, width):
#     self.length = length
#     self.width = width


#   def area(self):
#     return self.length*self.width

# class square(rectangle):
#   def __init__(self, side_length):
#     super().__init__(side_length, side_length)

#   def areaofsquare(self):
#     return super().area()

# rect = rectangle(3,2)
# squ = square(3)

# print("area of rectangle:", rect.area())
# print("area of square:", squ.areaofsquare())




# def divide():
#   try:
#     x = int(input("enter the number for x"))
#     y = int(input("enter the number for y"))
#     result = x/y
#     print("result", result)

#   except ZeroDivisionError:
#     print(f"general exemption{ZeroDivisionError}")
#     x = int(input("enter the number for x"))
#     y = int(input("enter the number for y"))
#     result = x/y
#     print("result from zero division error", result)

#   except ValueError as e:
#     print("invalid input")
#     x = int(input("enter the number for x"))
#     y = int(input("enter the number for y"))
#     result = x/y
#     print("result from value error", result)


#   except Exception as e:

# divide()
# try:
#   print(x)
# except NameError as e:
#   print(" it is name error {e}")

# a =1 
# b = "abc
# result = a + 


# try:
#   a = 4
#   b = "abc"
#   sum1 = a + b
#   print(sum1)

# except TypeError as e:
#   print(f"type erroe{e}")

# lst = [1, 2, 3]
# print(lst[30])
# list = [1,2,3]
# try:
#   print(list[30])
# except IndexError as e:
#   print("invalid index")

# import traceback 
# student = {
#   "name" : "abc"
#   }
# try:
#   student["class"]
# except KeyError as e:
#   traceback.print_exc()
#   print("invald key")

# class negative_error(Exception):
#   def __init__(self, message):
#     super().__init__(message)

# class zero_error(Exception):
#   def __init__(self, message):
#     super().__init__(message)

# try:
#   x = -1
#   if x < 0:
#     raise Exception("sorry, no number below zero")
#   if x == 0:
#     raise Exception("sorry, zero error")
# except negative_error as e:
#   print(e)
#   print("x value is negative")

# except zero_error as e:
#   print(e)
#   print("x value is zero")

# class negative_error(Exception):
#   def __init__(self, message):
#     super().__init__(message)

# class zero_error(Exception):
#   def __init__(self, message):
#     super().__init__(message)

# try:
#   x = int(input("the age"))
#   if x < 0:
#     raise Exception("sorry, no number below zero")
#   if x > 1000:
#     raise Exception("sorry, no number above 1000")
# except negative_error as e:
#   print(e)
#   print("x value is negative")

# except zero_error as e:
#   print(e)
#   print("x value above 1000")

# file = open('C:/Users/Dell/Documents/ram.txt','r')
# a = file.read()
# print(a)
# file.close()

# with open('C:/Users/Dell/Documents/ram.txt','r') as file:
#   a = file.read()
#   x = a.split()
#   for i in x:
#     if "welcome" in x:
#       print(x)

# with open('data.csv','r') as file:
#   line1 = file.readline()
#   for i in range(1, len(line1) ):
#     print(lin)

#   print(line1)
#   print(type(line1))
#   line2 = file.readline()
#   print(line2)


# file_path = 'raj.txt'
# with open(file_path, 'a') as file:
#   file.write("appending new line\n")


# file_path = 'raj.txt'
# with open(file_path, 'w') as file:
#   file.write("Hello, world\n")

# file_path = 'raj.txt'
# with open(file_path, 'x') as file:
#   file.write("Hello, world\n")

# while True:
#     username = input("enter the name:")
#     age = int(input("enter the age:"))
#     adress = input("enter the adress:")

#     try:
#       with open("data.csv", 'a') as file:
#         file.write(f"\n{username},{age},{adress}")
#         print("data added successfully")

#     except FileExistsError as e:
#       print("file doesnot exixt please check path of the file")

# while True:
#     username = input("enter the name:")
#     age = int(input("enter the age:"))
#     adress = input("enter the adress:")

#     try:
#       with open("data.csv", 'w') as file:
#         file.write(f"{username},{age},{adress}\n")
#         print("data added successfully")
#         break

#     except FileExistsError as e:
#       print("file doesnot exixt please check path of the file")

# import csv
# file_path = 'data.csv'
# with open(file_path, mode = '')

# import csv
# data = [
#     ['alice',30,'london'],
#     ['bob',25,'paris'],
#     ['charlie',35,'berlin']
# ]
# file_path = 'abc.csv'
# with open(file_path, mode ='w', newline = '') as file:
#   csv_writer = csv.writer(file)
#   csv_writer.writerow(['name','age','city'])
#   for row in data:
#     csv_writer.writerow(row)

# import csv
# file_path = 'data.csv'
# with open(file_path, mode ='r') as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row)
# import csv
# data = [
#     {'name':'alice','age':'30','city':'london'},
#     {'name':'sam','age':'35','city':'londona'},
#     {'name':'ranjan','age':'80','city':'londonm'}
# ]
# file_path = 'output.csv'
# fieldnamesss =['name','age','city']
# with open(file_path, mode='w', newline = '') as file:
#     writer = csv.DictWriter(file, filenames = fieldnamesss)
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)

# import module
# module.greeting("ram")
# module.sum(1,2)
# module.diff(6,1)
# from module import sum
# x = sum(2,5)
# import pandas as pd
# data = {'name': ['alice','bob','ram'],
# 'age':[20,23,13],
# 'city':['birgubj','ktm','pokhra']}
# df = pd.DataFrame(data)
# print(df)
# import pandas as pd
# df = pd.read_csv('aaa.csv')
# for x in df.index:
#   if df.loc[x,"Duration"] > 120:
#     df.loc[x, "Duration"] = 120
# print(df)

# import pandas as pd
# data = {'name': ['alice','bob','ram'],
# 'age':[20,None,13],
# 'date':['2020/12/01','2022/12/01','2020/8/01']}
# df = pd.DataFrame(data)
# print(df)
# for x in df.index:

#     if str(df.loc[x,"age"]) == "nan":

#         df.loc[x,"age"] = 30
# print(df)
# import pandas as pd
# df = pd.read_csv('aaa.csv')
# for x in df.index:
#     if df.loc[x,"Duration"] >120:
#         df.drop(x, inplace = True)
# print(df)
# import pandas as pd
# df = pd.read_csv('aaa.csv')
# print(df.duplicated())
# df.drop_duplicates(inplace = True)
# print(df)

# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2,3,5,7,11]

# x1 = [6,7,8,9,10]
# y1 = [2,3,5,7,11]

# plt.plot(x,y, marker = 'o', linestyle = '--', color = 'b', label = 'Prime Numbers')

# plt.plot(x1,y1, marker = 'o', linestyle = '--', color = 'b', label = 'Prime Numbers')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# plt.title('Prime Numbers Plot')
# plt.legend()
# plt.show()

#snowsite - data visualization tool
#tableau - data visualization tool but complex
#microsoft powerbi - data visualization tool - easy one


# import pandas as pd
# df = pd.read_csv('aaa.csv')
# print(df)
# print(df.to_string())
# import pandas as pd
# data = {
#   'name': ['ram','hari','shyam'],
#   'age': [12,20,45]
# }
# a = pd.DataFrame(data)
# #print(a)
# print(a.loc[[1,2]])
# import pandas as pd 
# print(pd.__version__)
# import pandas as pd

# a = [1, 7, 2]


# myvar = pd.Series(a, index = ['x','y'])

# print(myvar)

# import pandas as pd
# print(pd.options.display.max_rows)
# import pandas as pd
# pd.options.display.max_rows = 9999
# df = pd.read_csv('D:/customers-1000.csv')
# print(df)
# import pandas as pd
# df = pd.read_json('C:/Users/Dell/Downloads/sample2.json')
# print(df)

# import pandas as pd

# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# df = pd.DataFrame(data)

# print(df) 

# import pandas as pd
# df = pd.read_csv("aaa.csv")
# #print(df.tail())
# print(df.info())

# import pandas as pd
# df = pd.read_csv('aaa.csv') 
# print(new_df.to_string())

# import pandas as pd
# df = pd.read_csv('aaa.csv')
# df.dropna(inplace = True)
# print(df.to_string())

# import pandas as pd
# df = pd.read_csv('aaa.csv')
# df.fillna(130, inplace = True)
# print(df)

# import pandas as pd
# df = pd.read_csv('aaa.csv')
# df["Calories"].fillna(130, inplace = True)
# print(df)

# import pandas as pd
# df = pd.read_csv('aaa.csv')
# x= df["Calories"].mode()[0]
# df["Calories"].fillna(x, inplace = True)
# print(df)


# import pandas as pd
# df = pd.read_csv('aaa.csv')
# df.dropna(subset = ['Date'], inplace = True)
# print(df)


# import pandas as pd
# df = pd.read_csv('aaa.csv')
# df.loc[7,'Duration'] = 45
# print(df)

# import pandas as pd
# df = pd.read_csv('aaa.csv')
# for x in df.index:
#     if df.loc[x,'Duration'] > 120:
#       df.loc[x,'Duration'] = 120
# print(df)

# import pandas as pd
# df = pd.read_csv('aaa.csv')
# for x in df.index:
#     if df.loc[x,'Duration'] > 120:
#         df.drop(x, inplace = True)
# print(df)

# import pandas as pd
# df = pd.read_csv('aaa.csv')
# print(df.duplicated())

# import pandas as pd
# df = pd.read_csv('aaa.csv')
# df.drop_duplicates(inplace = True)
# print(df)
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('aaa.csv')
# df.plot()
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('aaa.csv')
# df.plot(x = 'Duration', y= 'Calories')
# plt.show()

# import pandas as pd
# df = pd.read_csv('aaa.csv')
# df['Date'] = pd.to_datetime(df['Date'], format = "mixed")  #not working
# print(df.to_string())
# print(df)

# numbers = [1,2,3,4,5]
# squared = list(map(lambda x: x**2, numbers))  # syntax, map(function, iterable/list)- executes specified function for each item in an iterable manner
# print(squared)

# def sq(x):
#     return x**2

# lst = [1,2,3]
# squared = list(map(sq, lst))

# def num(x):
#     if x % 2 == 0:
#         return x
#     # if x % 2 != 0:
#     #     return x
# lst = [1,2,3,4,5,6]
# even1 = list(map(num,lst))
# print(even1)

# # def num(x):
#     if x % 2 == 0:
#         return False
# lst = [1,2,3,4,5,6]
# even = list(filter(num,lst)) # filter snytax, filter(function, itearable/list)- executes either true or false
# print(even)

# from functools import reduce
# def num(x,y):
#     x = x + y
#     return x
# lst = [1,2,3,4,5]
# sum = reduce(num,lst) # reduce retrurn a single value
# print(sum)

# from functools import reduce
# def num(x,y):
#     if x > y:
#         return x
#     else:
#         return y
# lst = [1,2,3,4,5]
# greater_value = reduce(num,lst)
# print(greater_value)
   
# numbers = [1, 2,3, 4,5]
# sqaured = list(map(lambda x: x**2, numbers) )
# print(sqaured)

# def num(x):
#   y = x**2
#   return y
# lst = [1,2,3,4,5]
# squared = list(map(num,lst))
# print(squared)

# def num(x):
#   if x % 2 == 0:
#     y = x
#     return y
# lst = [1,2,3,4,5,6,7]
# evennum = list(map(num,lst))
# print(evennum)

# numbers = [1,2,3,4,5,6,7,8]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# def num(x):
#   if x % 2 == 0:
#     return False
# lst = [1,2,3,4,5,6]
# even_number = list(filter(num, lst))
# print(even_number)
# from functools import reduce 
# numbers = [1,2,3,4,5,6,7,8]
# sum = reduce(lambda x,y : x+y, numbers)
# print(sum)

# from functools import reduce 
# def sum(x,y):
#   x = x+y
#   return x
# lst = [1,2,3,4,5,6]
# sum1 = reduce(sum,lst)
# print(sum1)
# from functools import reduce
# numbers = [1,2,3,4,5,6,7,8]
# greatest_number = reduce(lambda x,y: x if x>y else y, numbers)
# print(greatest_number)
# from functools import reduce
# def num(x,y):
#   if x>y:
#     return x
#   else:
#     return y
# lst = [1,2,3,4,5,6,7]
# greatest_number = reduce(num,lst)
# print(greatest_number)

# from functools import reduce
# words = ["hello"," ","world","!"]
# concatenated_string = reduce(lambda x,y: x+y, words)
# print(concatenated_string)

# from functools import reduce
# def str(x,y):
#   x = x+y
#   return x
# words = ["hello"," ","world","!"]
# constr = reduce(str,words)
# print(constr)
# from functools import reduce
# numbers = [1,2,3,4,5,6,7,8]
# product = reduce(lambda x,y: x*y,numbers,1)
# print(product)

# import mysql.connector
# install sqlite
# install sqlite viewer
# install sqlite3editor

# import sqlite3

# conn = sqlite3.connect('abc.db')
# c= conn.cursor()
# c.execute('CREATE TABLE IF NOT EXISTS usres (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, email Text)')
# conn.commit()
# conn.close()

# import sqlite3

# conn = sqlite3.connect('abc.db')
# c= conn.cursor()
# name = "rabi"
# age = 45
# email = "ict.dhm@gmail.com"
# c.execute('insert into usres (name,age,email) values(?,?,?)',(name,age,email))
# conn.commit()
# usres = [("syam", 43, 'ict.ddcbara.com'),
#          ("rani",56,"ict.rail.com")]
# c.executemany('insert into usres (name,age,email) values(?,?,?)',usres)
# conn.commit()
# c.execute("UPDATE usres SET age = 100 WHERE name = 'syam'")
# conn.commit()
# c.execute("DELETE FROM usres WHERE name = 'syam'")
# conn.commit()
# c.execute("select * from usres")
# rows = c.fetchall()
# print(rows)
# for row in rows:
#     print(row)

# c.execute("select *from usres where age > 50")
# filtered_rows = c.fetchall()
# print(filtered_rows)



# print("\n=== CRUD Application Menu ===")
# print("1. Create Record")
# print("2.Read Record")
# print("3.Update Record")
# print("4.Delete Record")
# print("5.Exit")

# import sqlite3
# x = sqlite3.connect('project2.db')
# c = x.cursor()

# c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, email Text)')
# x.commit()

# option = int(input("enter the option"))

# if option == 1:
#     name = input("enter the name")
#     age = int(input("enter the age"))
#     email = str(input("enter the email"))
#     c.execute('insert into users (name,age,email) values(?,?,?)',(name,age,email))
#     x.commit()
    
# if option == 2:
#     c.execute("select * from users")
#     rows = c.fetchall()
#     print(rows)

# if option == 3:
#     email1 = str(input("enter the email"))
#     c.execute("UPDATE users SET age = 100 WHERE email = (?)",(email1,))
#     x.commit()
    
# if option == 4:
#     age = int(input("enter the age"))
#     c.execute("DELETE FROM users WHERE age = '43' ")
#     x.commit()

# if option == 5:
#     print("this line will not be executed")
#     quit()


import datetime
print("choose 1 for entery details and 2 for exit details")
choice = int(input("enter the choice"))
import sqlite3
x = sqlite3.connect('PROJECT4.db')
c = x.cursor()
if choice == 1:
  while True:   
    

    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, phone INTEGER, vehiclenumber TEXT, entrytime datetime.datetime, exittime TEXT, totalprice INTEGER, vehicletype TEXT)')
    x.commit()


    username = input("enter the name")
    phone = int(input("enter the mobile number"))
    vehiclenumber = str(input("enter the vehicle number"))
    
    entrytime = datetime.datetime.now()
    exittime = 0
    totalprice = 0
    print(" preess 1 for two wheeler and 2 for four wheeler \n" )
    option = int(input("enter the option"))
    if option == 1:
      vehicletype = "two wheeler"
    if option == 2:
      vehicletype = "four wheeler"


    c.execute('insert into users (username,phone,vehiclenumber,entrytime,exittime,totalprice,vehicletype) values(?,?,?,?,?,?,?)',(username,phone,vehiclenumber,entrytime,exittime,totalprice,vehicletype))
    x.commit()
    print("data added successfully")

    c.execute("select * from users")
    rows = c.fetchall()
    print(rows)
    with open('kalu.txt', 'w') as file:  # The output file name 
  
      file.write(', '.join(map(str, rows)) +'\n')


if choice == 2:
  
  input_id = int(input("enter the idnum"))
  
  t = datetime.datetime.now()
  print(type(t))
  
  c.execute("UPDATE users SET exittime = (?) WHERE id = (?)",(t,input_id))
  x.commit()

  c.execute("select * from users WHERE id = (?)",(input_id,)) # to print one specific id data
  x.commit()
  rows = c.fetchall()
  for row in rows:
    print(row)
    
  print("_____________",row)
  print(type(row[4]))
  print(row[5])
  print(type(row[4]))
  
  time_difference = datetime(row[5]) - datetime(row[4])
  print(time_difference)





  # time_difference = row[4] - t
  # print(time_difference)



  # c.execute("select * from users")
  # rows = c.fetchall()
  # for row in rows:
  #  print(row)
  


#   # c.execute("SELECT * FROM users WHERE id = input_id")
#   c.execute("update users SET exittime = 0 WHERE id = (?)",(input_id,))
#   x.commit()
#   rows = c.fetchall()
#   for row in rows:
#     print(row)


  # exittime = datetime.datetime.now()
  # c.execute('insert into users (exittime) values(?)',(exittime))
  # x.commit()
  # p = "select * from users Where id = input_id"
  # print(p)
  
  
  # exittime = datetime.datetime.now()
  # print(exittime)
  # total_time = entrytime - exittime
  # print(total_time)



