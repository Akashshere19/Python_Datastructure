# import array
# my_array= array.array('i',[1,2,5,2])
# my_array.extend([7])
# print(my_array)
# print(len(my_array))
# import numpy as np
# no_array = np.array([],dtype = int)

# print(no_array)

############### search element in array
# import array 
# my_array = array.array('i',[1,2,3,6])
# def lin_fun(arr,target):
#   for i in range(len(arr)):
#     if arr[i] == target:
#       return i
#   return "element not found"

# print(lin_fun(my_array,6))       


"""# 1.create array and traverse
from array import *
my_array = array('i',[1,7,2,4,5,5])
for i in my_array:
  print(i)

# 2. Access indivial element through indexes
print(my_array[3])

# 3.Append any value in array using append method

my_array.append(6)
print(my_array)
# 4.insert any value in array using insert method
my_array.insert(2,9)
print(my_array)
# 5. extend any value in array using extend method
l1= [56,23]
my_array.extend(l1)
print(my_array)
# 6.add item from list into array using fromlist method
tempList = [20,21,23,20,5]
my_array.fromlist(tempList)
print(my_array)
# 7. remove array element using remove method
my_array.remove(20)
print(my_array)
# 8.remove array element using pop method
my_array.pop()
print(my_array)
# 9.fetch any element's index  using index method
print(my_array.index(21))
# 10. reverse python array using reverse method
my_array.reverse()
print(my_array)
# 11. get array buffer information through buffer_info method
print(my_array.buffer_info())
# 12. check for number of occurences of an element using count method
print(my_array.count(5))
# 13. convert array to python list with same elements using tolist method
print('13 step')
strList = my_array.tostring()
print(type(strList))
ints = array('i')
ints.fromstring(strList)
print(ints)
# 14. convert array to python list with same elements using tolist method

print(my_array.tolist())
# 15. append string to char array using fromstring method

# 16. slice element from array
print(my_array[3:6]) """

"""
# create and insert two dimension array
import numpy as np
two_Array = np.array([[12,34,5],[12,32,11],[15,18,23],[21,45,65]])
print(two_Array)

newTwoArray = np.insert(two_Array,0,[[1,2,8,7]],axis=1)
print(newTwoArray)

newTwoArray= np.append(two_Array,[[1,3,7]],axis=0)
print(newTwoArray)"""

"""
# access element of two dimension array
import numpy as np
twoArray = np.array([[12,34,5],[12,32,11],[15,18,23],[21,45,65]])
print(twoArray)

def accessElements(array,rowIndex,colIndex):
  if rowIndex >=len(array) or colIndex >= len(array[0]):
    print('Incoorect Index')

  else:
    print(array[rowIndex][colIndex])

accessElements(twoArray,1,4)    """


