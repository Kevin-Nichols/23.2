def number_count(nums):
    res = {}
    nums = str(nums)
    for num in nums:
        res.update({num: res.get(num, 0) + 1})
    return res

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return number_count(num1) == number_count(num2)
    