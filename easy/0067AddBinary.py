'''
67. Add Binary
Solved
Easy
Topics
Companies

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

 

Constraints:

    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.


'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert the binary strings to integers using base 2
        num = int(a, 2) + int(b, 2)
        
        # Handle the edge case where the sum is 0
        if num == 0:
            return "0"
        
        result = ""
        # Convert the sum back to a binary string
        while num > 0:
            result = str(num % 2) + result
            num //= 2
        return result
