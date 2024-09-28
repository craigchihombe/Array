import array as arr
array_num = arr.array('d',[1,2,3,4,5,4,6,7])
print("original array: "+str(array_num))
print("number of occurance of the number 4 in the given array: "+str(array_num.count(4)))
array_num.reverse()
print("Reverse the order of the items in the array")
print(str(array_num))
