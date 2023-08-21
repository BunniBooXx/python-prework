# Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of
#the function

def hello_name(user_name): 
    print("hello_ " + user_name + "!")

hello_name ('USERNAME')

# Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns 
# nothing 

def first_odds():
  first_odds= list (range (1,100,2))
  print(first_odds)
first_odds ()    

# Question 3: Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list): 
    print ("Max: ", max(a_list))
max_num_in_list([1,2,3,4])

# Question 4: Write a function to return if the given leap year. A leap year is divisible by 4,
# but not divisible by 100 unless it is also divisible by 400. The return should be boolean type 
# (True/False)

def is_leap_year(a_year):
     if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
          return True
     else: 
          return False 
a_year1= 2020
a_year2= 2017

print(is_leap_year(a_year1))
print(is_leap_year(a_year2))

# Question 5: Write a function to check to see if all numbers in list are consecutive numbers. For 
# Example [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return
# Should be boolean Type.

def is_consecutive(a_list): 
   prev_nums = []
   for num in a_list:
      if not prev_nums:
         prev_nums.append(num) 
      elif num == prev_nums[-1]+1:
         prev_nums.append(num)
      else: 
         return False   
   return True
print(is_consecutive(a_list = [1,2,3,4,5]))