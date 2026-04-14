class Solution:
    def ToggleCase(self, s):
        # Uppercase and lowercase letters differ by 32 in ASCII. XOR with 32 flips that specific bit, 
        # converting uppercase to lowercase and vice versa. It’s an O(n) approach but less readable than built-ins like swapcase()
        #s.swapcase()
        return "".join(chr(ord(ch) ^ 32) for ch in s)
