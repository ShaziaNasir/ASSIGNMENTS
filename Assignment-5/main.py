#comparision operators & logical operators

# specific_time:int=3
# ingredients=["milk","yougrut","sugar"]
# if specific_time==3 and ingredients==["milk","yougrut","sugar"]:
#  print("getup for iftari preparation")
# elif specific_time<3 and ingredients!=["milk","yougrut","sugar"]:
#  print("go to the market and buy things")
# else:
#  print("this matter will be handled by mother")

# # loops 1.for loops & 2.while loop
# Boys_name:str=["Ali","Saad","Shahzeb"]
# for Boy_name in Boys_name:
#  print(Boy_name,"You are invited")

#  count:int=1
#  while count<=10:
#   print("Iam grate ful to you")
#   count+=1

#control 1.break  2.continue  3.pass
 

# for i in range(3):
#   x=int(input("please enter your number between 1 and 100 which should be even"))
#   if x%2==0:
#     print ("valid no",x)
#     break
#   else:
#     print("in valid number ,Try again")

# for _ in range(10): # Just to show that _ is a loop variable, but its throwaway variable
#     # Code to be executed 100,000 times
#      print(f"Hello, World! Iteration { _ }")


# for i in range(3):
#   x=int(input("please enter your number between 1 and 100 which should be even"))
#   if x%2==0:
#     print ("valid no",x)
#     continue
#   else:
#     print("in valid number ,Try again")

#practice questions
#q1:wap ta ask the user to enter names of their 3 favourite movies and store them ina list
# x=str(input("please enter your first movie"))
# y=str(input("please enter your second movie"))
# z=str(input("please enter your third movie"))
# print([x]+[y]+[z])
    
#q2 wap to check if a list contains a palindrome of elements
# x=[1,2,3,2,1]
# y=[1,2,3]
# copy_x=x.copy()
# copy_y=y.copy()
# reverse_x=copy_x.reverse()
# reverse_y=copy_y.reverse()
# if {copy_x==reverse_x}:
#  print("list is palindrome")
# else:
#  print("list is not palindrome")

#q3 wap to count the number of students with the "A" grade in the following tuple
# grades=("C","D","A","A","B","B","A")
# count_grades=grades.count("A")
# print(count_grades)

#q4store the above values in a list and sort them from "A"to "D"
# grades=["C","D","A","A","B","B","A"]
# grades.sort()
# print(grades.sort())

#q5.waf to print the length of a list.(list is the parameter)
# def cal(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# cal(3,4)

# fruits=["mango","pear","banana","orange"]
# def print_len(list):
#     print(len(list))

# print_len(fruits)

#waf to print the elements of a list in a single line.(list is the parameter)
# list_1=[1,2,3,4]
# list_2=[5,6,7,8,9]
# def list(list_1,end=list_2):
#     print(list_1,list_2)

# print(list_1,list_2)

# print(list_1[0], end="  ")
# print(list_2[2], end="  ")

#question to write afunction which shows even and odd as a out put
x=int(input("please enter your number"))

def check(number):
    if {number/2==0}:
        print("number is even")
    else:
        print("number is odd")

        return x
check(x)





 