# Problem: https://leetcode.com/problems/contains-duplicate/
# Solution: https://leetcode.com/problems/contains-duplicate/solutions/2921/contains-duplicate/

def item_in_common(arr1, arr2):
    """
    Given two arrays, return True if they have at least one common item.
    """
    # Convert the first array to a set for O(1) lookups
    set_arr1 = set(arr1)
    
    # Iterate through the second array and check if any item is in the set
    for item in arr2:
        if item in set_arr1:
            return True
    return False

def contains_number(arr1, arr2):
    my_dict = {}
    for i in arr1:
        my_dict[i] = True
    for j in arr2:
        if j in my_dict:
            return True
    return False
