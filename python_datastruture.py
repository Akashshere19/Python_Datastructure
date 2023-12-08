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

"""# treaversing two dimension array

import numpy as np
twoArray = np.array([[12,34,5],[12,32,11],[15,18,23],[21,45,65]])
print(twoArray)
def traveseArray(array):
  for i in range(len(array)):
     for j in range(len(array[0])):
       print(array[i][j])


traveseArray(twoArray)"""
"""
# search in twodimension array
import numpy as np
twoArray = np.array([[12,34,5],[12,32,11],[15,18,23],[21,45,65]])
print(twoArray)
def serachTDArray(array,value):
  for i in range(len(array)):
    for j in range(len(array[0])):
      if array[i][j] == value:
         return "value is at index "+ str(i)+" "+str(j)

  return "element is not found" 

print(serachTDArray(twoArray,45))    """

"""# Deleting in two dimension array

import numpy as np
twoArray = np.array([[12,34,5],[12,32,11],[15,18,23],[21,45,65]])
print(twoArray)
newArray = np.delete(twoArray,0,axis=1)
print("new array:")
print(newArray)"""

######################## List ############################
"""
# accessing/traversing list
lst1 = ['python','java','c++','php']
print(lst1)
# print(len(lst1))
# print(lst1[2])
# print('c++' in lst1)
# print(lst1[-2])
# print(lst1[-1:-2:-1])
for i in range(len(lst1)):
  lst1[i] = lst1[i]+ " advance"
  print(lst1)

empty = []
for i in empty:
  print("it is none")  """

"""
# Update/Insert list

lst1 = [3,1,9,5,7,2]
print(lst1)
# lst1[2]='hello'
# print(lst1)
# lst1[4] = 4.3
# print(lst1)
bye = 467
lst1.insert(4,bye)
print(lst1)

lst1.append(89)
print(lst1)

lst1.extend([9,3,'say'])
print(lst1)"""

# Slice in list
lst1 = [3,1,9,5,7,2]
print(lst1[0:4:])
lst1[1:3] = ['a','c','t',2] # add list in 1st list
print(lst1)


# lst1.pop()
# print(lst1)
# l = lst1.pop(3)
# print(l)
# print(lst1)

# del lst1[3]
# print(lst1)
# del lst1[1:3]
# print(lst1)

# lst1.remove(2) # required element
# print(lst1)
# lst1.remove(2)
# print(lst1)

"""
#searching element in list
tar  = 5
if tar in lst1:
  print('this element is in list')

else:
  print('not found')

# linear search

def linear_search(p_list,p_tar):
    for i,value in enumerate(p_list):
      if value  == p_tar:
        return i
    return -1

print(linear_search(lst1,tar)) """

"""
lst_1st = [2,5,8,3,6,9]
lst_2nd = [5,89,10,12,15]

con_lst = lst_1st + lst_2nd
print(con_lst)"""

"""
# Operators in list
lst = [2,5,6,0,-7,-8]
print(lst * 4)

print(len(lst))
print(max(lst))
print(min(lst))
print(sum(lst))"""

"""
strr = 'string string split'

lst = list(strr)
print(lst)
print(strr.split())

b = 'string-string-split'
delimiter = 'a'
str1 = b.split(delimiter)
print(str1)
print(delimiter.join(str1)) """

"""lst = [2,9,12,6,7,4]
lst.sort()
print(lst)
lst.append([3,9,5])
print(lst)"""

# list comprehnsion

lst = [3,7,2]
new_lst = []
for i in lst:
  mult_2 = i * 2
  new_lst.append(mult_2)

print(new_lst)  
