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


class SEStaff:
    def __init__(self, name, role):
      self.name = name
      self.role = role

    def getName(self):
      print(self.name)

    def baka(self,input_name):
      print(input_name + ' is_baka')



stanley = SEStaff('stanley', 'programmer')
stanley.getName()
stanley.baka('stanley chau')
reika = SEStaff('reika', 'developer ')
print(reika.role + reika.name)

# print(stanley.name)


##set and dictionary


