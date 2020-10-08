class Solution(object):
    def isPalindrome(self, x) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        
        # Solution 1
        # for i in range(len(x_str)):
        #     if(x_str[i] != x_str[len(x_str) - 1 - i]):
        #         return False
        # return True
    
        # Solution 2
        return x_str[:: -1] == x_str