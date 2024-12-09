# def sum(x,y):
#     p = x + y
#     print(p)
#     return p
# 
# try:
#     print(p)
# except NameError:
#     print("variable is not defined")

# try:
#     file = ("fileexercise.txt", 'w')
#     try:
#         file.write("i love mango")
#     except:
#         print("something went wrong while writing to file")
#     finally:
#         file.close()
# except:
#     print("something went wrong while opening file")

x = -1
if x < 0:
    raise Exception("sorry, no number below zero")