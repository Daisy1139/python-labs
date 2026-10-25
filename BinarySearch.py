## Binary Search: find the index of target in a SORTED list
## Return the index if found, otherwise return -1
## Example: lst = [2, 3, 5, 6, 7, 9, 14], target 3 -> index: 1, target 4 -> -1

def binarySearch(my_lst, target):
    low = 0
    high = len(my_lst)-1
    while low <= high:
        middle = (low + high)//2
        if my_lst[middle] == target:
            return middle
        else:
            if my_lst[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
            
        
    return -1



## TESTING FUNCTION ONLY
## DO NOT WRITE YOUR CODE HERE
def test(my_lst, target, expected):
    result = binarySearch(my_lst, target)
 
    if result == expected:
        print("PASS: binarySearch(" + str(my_lst) + ", " + str(target) + ") =", result)
    else:
        print("FAIL: binarySearch(" + str(my_lst) + ", " + str(target) + ")")
        print("Your result:", result)
        print("Expected:   ", expected)
 
 
lst = [2, 3, 5, 6, 7, 9, 14]
 
## found
test(lst, 3, 1)       # normal case
test(lst, 6, 3)       # target is exactly the first middle -> found in 1 round
test(lst, 2, 0)       # first item  (left edge)
test(lst, 14, 6)      # last item   (right edge)
 
## not found
test(lst, 4, -1)      # between two items
test(lst, 1, -1)      # smaller than everything
test(lst, 20, -1)     # bigger than everything
 
## edge cases
test([], 5, -1)       # empty list -> loop never runs
test([7], 7, 0)       # one item, found
test([7], 8, -1)      # one item, not found
 