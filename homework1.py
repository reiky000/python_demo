src_arr = 'banana'
#output: 'ananab'
#how to creat an arr = ['b', 'a', 'n', 'a', 'n', 'a']
# some function in arr/loop


# arr = ['b', 'a', 'n', 'a', 'n', 'a']
# new_arr = []
# empty = ''
# for x in range(len(arr)):
#     new_arr.append(arr[-1])
#     arr.pop(-1)
# print(new_arr)


# arr.pop(0)
# arr.append('b')
#
# print(arr)

arr = ['b', 'a', 'n', 'a', 'n', 'a']
outputStr = ""
strLen = len(arr)

for i in range(strLen):
    outputStr = arr[i] + outputStr
print(outputStr)



