"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
"""
Here’s the algorithm for validating the brackets using only a stack, without any dictionary:

### Algorithm:
1. **Initialize an empty stack**:
   - This stack will hold opening brackets as we encounter them.

2. **Iterate through each character `char` in the string `s`**:
   - **If `char` is an opening bracket** (`(`, `{`, or `[`):
     - Push `char` onto the stack.
   - **If `char` is a closing bracket** (`)`, `}`, or `]`):
     - **Check if the stack is empty**:
       - If the stack is empty, return `False` (there is no corresponding opening bracket for this closing bracket).
     - **Pop the top element from the stack**:
       - **If the popped element does not match the expected opening bracket** for the current `char`:
         - Return `False`. For example, if `char` is `)` and the popped element is not `(`, it is a mismatch.

3. **After the loop**:
   - **Check if the stack is empty**:
     - If the stack is empty, return `True` (all brackets were matched correctly).
     - If the stack is not empty, return `False` (some opening brackets were not closed).

### Example Walkthrough
For the input `"({[]})"`:
   - Start with an empty stack.
   - For each character:
     - Push opening brackets onto the stack.
     - Pop and check closing brackets.
   - If all pairs match correctly, the stack will be empty at the end, and the function will return `True`.

This algorithm ensures that every opening bracket has a corresponding closing bracket in the correct order, using only a stack to track unmatched opening brackets.
"""
#CODE
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif char == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif char == ']':
                if not stack or stack.pop() != '[':
                    return False
        
        # If stack is empty, all brackets were matched
        return len(stack) == 0
