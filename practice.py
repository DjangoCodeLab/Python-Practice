## Basic List Operations.
# Create a list of the first 10 odd numbers.
from operator import rshift


result = []
for i in range(10):
    if i%2!=0:
        result.append(i)
print(result)

# Write a Python program to find the maximum and minimum values in a list.
l1 = [3,8,2,5,9,5]
max = l1[0]
min = l1[0]
for i in l1:
    if(i>max):
        max = i 
    elif(i<min):
        min = i
    
print("The maxinum and minimum value of give list is:",max,min)
# Reverse a list without using the reverse() method.
print(l1[::-1])

# Check if a specific element exists in a list.
existing_value = 5
if (existing_value in l1):
    print(f"{existing_value} is there in given l1 list" )


# List Comprehensions
# Generate a list of squares of numbers from 1 to 20 using list comprehension.
square_of_list = [x**2 for x in range(1,20+1)]
print(square_of_list)

# Create a list of all vowels from a given string.
name = "Siddheshwar Ramesh Kapde"
vovels = "aeiou"
result = [each for each in name if each in vovels]
print(list(set(result)))

# Generate a list of all numbers divisible by 3 and 5 between 1 and 100.
divisible_number_list = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0 ]
print(divisible_number_list)

# Generate a list of all numbers divisible by 3 or 5 between 1 and 100.
divisible_number_list = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0 ]
print(divisible_number_list)

# Slicing
# Extract every third element from a list.
l2 =[23,34,22,344,565,43]
print(l2[::3])
# Write a program to split a list into two halves.
l3 = [4,32,4,56,6,7,54,4,32,13]
split_list = int(len(l3)/2)
first_half_list = l3[:split_list]
second_half_list = l3[split_list:]
print("First Half List:",first_half_list)
print("Second Half List:",second_half_list)

# Create a new list that contains the elements of the first half of a given list in reverse order.
print(first_half_list[::])
print(second_half_list[::-1])


# Nested Lists
# Write a program to flatten a nested list.
nested_list = [
    [1,2,4],
    [5,6,7]
]
result = []
for i in nested_list:
    for j in i:
        result.append(j)

print(result)

# using Comprehensions 
result = [y for x in nested_list for y in x]
print(result)

# Given a matrix (2D list), write a function to find the sum of each row.
matrix_list = [
    [3,4],
    [2,3]
]
result = []
for i in matrix_list:
    result.append(i[0] + i[1])
print(result)

# using Comprehensions 
result1 = [x[0]+x[1] for x in matrix_list]
print(result)

# Transpose a given 2D list (matrix).
transpose_list = [
    [2,4],
    [3,5]
]
result = [
    [],
    []
]
for i in transpose_list:
    result[0].append(i[0])
    
for j in transpose_list:
    result[1].append(j[1])
print(result)



