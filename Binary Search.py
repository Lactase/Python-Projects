def binary_search(list, target):
    # Sort the list
    list.sort()
    # Set the start and end points
    start = 0
    end = len(list) - 1
    # Create a while loop for binary search
    while (start <= end):
        # Finds the mid point of the list
        middle = (start + end) // 2
        # If the mid point is the target
        if (list[middle] == target):
            return True
        else: 
            # If the target is smaller than the mid point
            if (list[middle] > target):
                # Replaces the end point with point left of middle
                end = middle - 1 
            else:
                # Replaces the start point with point right of middle
                start = middle + 1
        
        
    # Returns false if the target is not in the list
    return False


list = [1,3,5,7,32,5,3,6,4,5,34534,5,3,52,56,3,4,36346,254]

print(binary_search(list,1))
print(binary_search(list,6))
print(binary_search(list,99))