## Task
Make a program that filters a list of strings and returns a list with only your friends' names in it.  
If a name has exactly **4 letters**, it’s a friend! Otherwise, it’s not.  
Keep the original order of names in the output.

### Examples
Input: ["Ryan", "Kieran", "Jason", "Yous"]  
Output: ["Ryan", "Yous"]

Input: ["Peter", "Stephen", "Joe"]  
Output: []

### Code
def friend(x):
    return [name for name in x if len(name) == 4]

# Category
Fundamentals
