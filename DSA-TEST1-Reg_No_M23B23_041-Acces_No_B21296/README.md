## Question 1

a) What type of data structure is being used to store the numbers in the code, and

-> It's an array thet is used to store number in this code
`lst=[14,8,...,11]`
why is this data structure suitable for the task?

-> i do think that this Data stucture is suitable for this task, in the way that it is easier to get access to any element  
b) The code initializes maxSum with the first element of the list. Can you explain
the significance of this initialization and how it affects the algorithm's
correctness?

-> As this algorithm seems like to get the maximum sum of sub array(or subset of this list) without repetition and jumping, the first element make the first subset of this list , thus it sum is logicaly itself

c) How does the for loop iterate through the list, and what is the purpose of the  
-> the loop is used to access any value in this list  
sumz variable?  
-> the sumz variable is like a temporary variable that store temporary sum during each loop, it get iterated each time during the loop
How is it being updated within the loop?
-> the next value of the list is being added to it

d) Explain how the code identifies the maximum subarray sum. What conditions trigger the update of the maxSum variable?  
-> to identify the maximum suarray sum , it compare the temporary sum `sumz` and the current sum `maxSum` ; if the maxSum is less that the temporary sum, the current sum became equal to the temporary sum `sumz`

e) What is the time complexity of this code for finding the maximum subarray
sum, and how does the choice of data structure and algorithm contribute to its
efficiency or performance  
the choice of a data stucture and algorith have a highly impact on the runtime of our program in the fact that (they are linked), same DS can give more accessibility to a x task while other cannot

## Question 2

we first initialized to lists :one for anglican another for catolic martyrs

-> to clear duplicate , we first check if a name is present on both list then we removed it

```
# first we looped thwoth one list using while:
while x is less than the len of that list:
    if the element at index x is present on the other list:
        remove it from the current list
        then we remove it to the other one

    the we increment x
```
