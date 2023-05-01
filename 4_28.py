#simple number reverse
# num_list = ["3","2","1"]
#
# num_list.reverse()
#
# print(num_list)

# num_arr = ["3","2","1"]
# num_str = ""
#
# for elm in num_arr:
#     num_str += elm
# #      num_str = num_str + elm
#
# print(num_str)
# # put in integer
# print(int(num_str))

# 210 to 012 to 12

# num_list2 = ["2","1","0"]
#
# num_list2.reverse()
# print(num_list2)
#
# zero = [i.lstrip('0') for i in num_list2]
# print(zero)

# -123 to -321
# num_list3 = ["-","3","2","1"]
#
# num_list3.reverse()
# print(num_list3)

# num1 = 1230
# num_list = list(str(num1))
#
# num_list.reverse()

#
# # land
#
# def function(x):
#     return lambda a: a * x
#
#
#
#
# value = function(10)
#
# print(value(5))


# Map function
# 2 each element in array
# fruit = ["apple", "banana", "grapes"]
# num_arr = [1, 2, 3, 4, 5]

# fruits = list(map(lambda x: x + 's', fruit))
#
# print(fruits)
# list needed otherwise they show us the memory
# ans = list(map(lambda y: y * 10, num_arr))
# print(ans)
# # [10, 20,]
#
# fruits =[]
# for elm in fruit:
#     new_elm = elm + 's'
#     fruits.append(new_elm)
#
# print(fruits)
#make it shoter time if it uses lambda or Map
#iterator loop through



# filter
# arr = []
# for x in range(1, 10):
#     arr.append(x)
# print(arr)
#
# ans = list(filter(lambda x: x <= 5, arr))
# print(ans)
