nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):

    return [num ** 2 for num in nums]

 

def remove_negatives(nums):

    return [num for num in nums if num > 0]

def choose_func(nums: list, func1, func2):
    itteration = 0
    
    for num in nums:
        itteration += 1
        
        if num < 0:
            print(func2(nums))
            break
        
        if itteration == len(nums):
            print(func1(nums))
            
choose_func(nums1, square_nums, remove_negatives)