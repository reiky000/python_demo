# x='hello'
# num1= 1
# num2= 1.1
# str1='10'
# str2 = 'hello'
#
#
# num3 = int(num2)
# word = 'a'
#
# print(x)
#
# print(type(x))
# print(type(num1))
# print(type(num2))
# print(num1 == num2)
# print(x == str2)
# print(num1 != num2)
# print(num3)



# arr1=[1,2,5,4,3]
# fruits = ['banana','apple', 'grape']
# fruit_name = 'pineapple'
# counter = 0
# arr1.sort()
# print(arr1[-1])

# arr1.append(7)®
# arr1.pop(1)

# print(arr1)
# for fruit in fruits:
#  print(fruit)

# for letter in fruit_name:
#  print(letter)

# for x in range(10):
#    print(x +1)

#
# for x in range(10):
#  # counter = counter +1
#  counter += 1
#  print(counter)

#
# while True:
#  counter += 1
#  print(counter)



# while True:
#  counter += 1
#  print(counter)
#  if counter >= 10:
#   break



# def function1(input_value):
#  x = 'banana'
#  print(input_value)
#  return x
#
# print(function1('hello'))


# def function1(input_value):
#  x = 'banana'
#  print(input_value)
#  return x
#
# res = function1('hello')
#
# print(res)


# class SEStaff:
#     def __init__(self, name, role):
#       self.name = name
#       self.role = role
#
#     def getName(self):
#       print(self.name)
#
#     def baka(self,input_name):
#       print(input_name + ' is_baka')
#
#
#
# stanley = SEStaff('stanley', 'programmer')
# stanley.getName()
# stanley.baka('stanley chau')
# reika = SEStaff('reika', 'developer ')
# print(reika.role + reika.name)
# print('hello')

# print(stanley.name)


##set and

# fruits_set = {"banana", "apple", "pineapple"}
# my_fav_fruit ={"grape", "apple"}
# fruit_arr = ["banana", "apple", "pineapple"]
# print(type(fruits_set))
# print(fruit_arr[0])
# print(fruits_set[0])
# print(fruits_set.intersection(my_fav_fruit))
# 二つのセットの中から同じものを出す

# new_set = fruits_set.union(my_fav_fruit)
# print(new_set)

# print(fruits_set.union(my_fav_fruit))

# fruits_set.add("banana")
# print(fruits_set)

# print(fruits_set.difference(my_fav_fruit))
#
# fruits_set.pop()
# print(fruits_set)
#
# print(my_fav_fruit.difference(fruits_set))

import math

# cnt =0
# time complexity(0^2)
# for x in range(10):
#     for y in range(10):
#         print(x, y)
#         cnt += 1
# print(8**2)
# print(math.ceil(11/5))
# print(math.floor(11/5))
# print(cnt)
#

# dictionary

person = {
    "name": "stanley",
    "age": 27,
    "job": "programmer"
}

print(person)
print(person["name"])