#!/bin/bash/python
#Practicing insertion sort
#By Diobolic

import random

#Initialize
unsorted_array = []
length = int(input("Please input length of array to sort: "))
count = 0

while count <= length:
    unsorted_array.append(random.randint(-10000,10000))
    count += 1

#Presort
print("Unsorted Array: " + str(unsorted_array))

#Sort
def my_sort(array_to_sort):
    
    output = []

    #Start Sorting
    while array_to_sort:

        minimum = array_to_sort[0]

        for number in array_to_sort:
            if number < minimum:
                minimum = number 
            
        output.append(minimum)
        array_to_sort.remove(minimum)

    return(output)



print("Sorting...")
output = my_sort(unsorted_array)

print(str(output))