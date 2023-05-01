# arr1 = [1, 2, 3, 4]
# arr2 = [2, 2, 3, 3]
# #
# # [1, 2, 2, 2, 3, 3, 3, 4]
#
# marge_arr = [*arr1, *arr2]
# print(marge_arr)
arr1 = [1, 2, 3, 4]
arr2 = [2, 2, 3, 3]
arr3 = arr1 + arr2
arr3.sort()
print(arr3)