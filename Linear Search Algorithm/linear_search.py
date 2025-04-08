#Linear search goes through each element in a list one by one until it finds the target

#Given a list of numbers and a target number, return the index of the target number. If not found, return -1.

def linear_search(arr, target):
    for i in range(len(arr)):
       if target == arr[i]:
           return i
    return -1
         
print(linear_search([5, 3, 7, 2, 9], 7))  
print(linear_search([1, 2, 3], 5))
