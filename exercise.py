# i = 0
# while i != 10:
#     i = i +1
#     print(i)
    

# sum = 0
# num = int(input("enter the number"))
# for i in range(1, num+1, 1):
#     sum = sum+i
#     print(i)
# print(sum)


# i = 1
# while i != 11:
#     out = 2
#     out = out*i
#     print(out)
#     i =i +1
# mul = 2
# for i in range(1, 11, 1):
#     sum = mul*i
#     print(sum)

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i % 5 == 0 and i >= 150 and i <=500:
#         print(i)

# num = 546677776
# i = 0
# while num != 0:
#     num = num % 10
#     i = i+1
# print(i)

# num = 75869
# count = 0
# while num != 0:
#     # floor division
#     # to reduce the last digit from number
#     num = num // 10

#     # increment counter by 1
#     count = count + 1
# print("Total digits are:", count)

# list1 = [10, 20, 30, 40, 50]
# #newlist1 = reversed(list1)
# # for i in newlist1:
# #     print(i)
# size = len(list1)
# print(size)
# Display a message “Done” after the successful execution of the for loop
# for i in range(5):
#     print(i)
# else:
#     print("Done") 2+22+222
# sum = 0
# start = 2
# for i in range(5):
#     print(start, end = "+")
#     sum = sum + start

#     start = start *10 + 2
# print("\n")
# print(sum)
# arr = []
# def multiple_length_arg(*a):
#     for i in a:
#         print(i)
        
# multiple_length_arg(12, 16, 67, 'ertt')

# def employee(name, salary = 90000):
#     print("Name", name, "salary", salary)
#     return salary


# s = employee("rajna")
# print(s)

# # s = "rajan"
# # p = s[0]
# # q = int(len(s))
# # r = int(q/2)
# # s = s[r]

# # sum = p + s 
# # t = s[q-1]
# # print(t)
# # print(sum)

# str1 = 'James'
# print("Original String is", str1)

# # Get first character
# res = str1[0]

# # Get string size
# l = len(str1)
# # Get middle index number
# mi = int(l / 2)
# # Get middle character and add it to result
# res = res + str1[mi]

# # Get last character and add it to result
# res = res + str1[l - 1]

# print("New String:", res)
# lower = []
# upper = []
# string = "RuiFGijPnH"
# for i in string:
#     if i.islower():
#         lower.append(i)
#     else:
#         upper.append(i)
# s = ''.join(lower + upper)
# print(s)
# m = "this is a man"
# k = m.split(' ')
# print(k)

# def find_digits_chars_symbols(sample_str):
#     char_count = 0
#     digit_count = 0
#     symbol_count = 0
#     for char in sample_str:
#         if char.isalpha():
#             char_count += 1
#         elif char.isdigit():
#             digit_count += 1
#         # if it is not letter or digit then it is special symbol
#         else:
#             symbol_count += 1

#     print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)

# find_digits_chars_symbols("tyhhj566788#$$%%FG5")

# s = "Xyz"
# s1 = s[::-1]
# s2 = "abcd"
# # l1 = len(s1)
# # l2= len(s2)
# # length = l1 if l1>l2 else l2
# # result = ""
# # for i in range(length):
# #     if i < l1:
# #         result = result + s1[i]
# #     if i < l2:
# #         result = result + s2[i]
# # print(result)
# p = s + s2
# print(p)

# for value in range(10):
#     if value == 5:
#         print("before break")
#         continue
#         print ("afterbb break")
# 

# def compare_string(s1, s2):
#     flag = True
#     for i in s1:
#         if i in s2:
#             continue
#         else:
#             flag = False
    
#     return flag
# p = compare_string("abcd", "abcd")
# print("japan nepal in nepal".count("nepal"))
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# s1 = list(filter(None, str_list))
# print(s1)

# import string

# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)

# new_str = str1.translate(str.maketrans('', '', string.punctuation))

# print("New string is ", new_str)

# import re

# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)

# # replace special symbols with ''
# res = re.sub(r'[^\w\s]', '', str1)
# print("New string is ", res)
# list1 = ["M", "na", "i", "Ke"] 
# list2 = ["y", "me", "s", "lly"]
# x = []
# for i ,j in zip(list1, list2):

#     p= i +j
#     print(p)
        
# list1 = [5, 20, 15, 20, 25, 50, 20]
# list2 = []
# for i in list1:
#     if i != 20:
#         list2.append(i)
# print(list2)
        
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# c = dict(zip(keys, values))
# print(c)

# ample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# # ample_dict.pop('age')
# # print(ample_dict)
# print(ample_dict.get)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# # class Student(Person): #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")

# p1 = Student("rajan","sah",200)
# print(p1.welcome())

# file = open("fileexercise.txt","r")
# #print(file.read())
# # print(file.readline())
# # print(file.readline())
# a = file.read()
# b= a.split()
# # print(b)
# for x in b:
#   if x == "fan":
#     print(x)

# file = open("fileexercise.txt", "a")
# file.write("\thoney is drinking water")
# file.close()

# file = open("fileexercise.txt", "r")
# for i in file:
#   print(i)
# # print(file.read())
# # file.close()

# file = open("fileexercise.txt", "w")
# file.write("i am a disco dancer")
# file.close()

# file = open("fileexercise.txt", "r")
# print(file.read())

# while True:
# #     username = input("enter the name:")
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

import csv
data = [
    ['alice',30,'london'],
    ['bob',25,'paris'],
    ['charlie',35,'berlin']
]
file_path = 'abc.csv'
with open(file_path, mode ='w', newline = '') as file:
  csv_writer = csv.writer(file)
  csv_writer.writerow(['name','age','city'])
  for row in data:
    csv_writer.writerow(row)

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

# def sq(x):
#   return x**2

# lst = [1,2,3]
# squared = list(map(sq, lst))
# print(squared)

# def num(x):
#     if x % 2 == 0:
#         return x
# lst = [1,2,3,4,5,6]
# even1 = list(map(num,lst))
# print(even1)

# def num(x):
#   if x % 2 == 0:
#     return False
# lst = [1,2,3,4,5,6]
# even = list(filter(num,lst)) # filter snytax, filter(function, itearable/list)- executes either true or false
# print(even)

# import module
# module.greeting("ram")
# module.sum(1,2)
# module.diff(6,1)
# from module import sum
# x = sum(2,5)
# import calculation as c
# # calculation.multiply(4,6)
# # a = [1,2,3,4,5]
# # calculation.evennum(a)
# print(c.person1["name"])
# # import mymodule
# mymodule.num()

# from calculation import person1
# print(person1['name'])

# from mymodule import sum
# x= sum(2,3)


def divide():
  try:
    x = int(input("enter the number for x"))
    y = int(input("enter the number for y"))
    result = x/y
    print("result", result)

  except ZeroDivisionError:
    print("division by zero eroor")
    x = int(input("enter the number for x"))
    y = int(input("enter the number for y"))
    result = x/y
    print("result from zero division error", result)

  except ValueError:
    print("invalid input")
    x = int(input("first number"))
    y = int(input("second number"))
    result = x/y
    print("result", result)

divide()

  # except ValueError as e:
  #   print("invalid input")
  #   x = int(input("enter the number for x"))
  #   y = int(input("enter the number for y"))
  #   result = x/y
  #   print("result from value error", result)


#   except Exception as e:

#     divide()
# try:
#   print(x)
# except NameError as e:
#   print(" it is name error {e}")
