## Task
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (`True` means present).

### Example
[True,  True,  True,  False,  
 True,  True,  True,  True,  
 True,  False, True,  False,  
 True,  False, False, True,  
 True,  True,  True,  True,  
 False, False, True,  True]  
# => 17

### Code
def count_sheeps(sheep):
    return sum(1 for s in sheep if s is True)

# Category
Fundamentals
