class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Solution 1
        str_x = str(x)
        reverse_str_x = []
        for i in range(1, len(str_x) + 1):
            if i == len(str_x) and str_x[-i] == '-':
                reverse_str_x.insert(0, '-')
            else:
                reverse_str_x.append(str_x[-i])
        x = int(''.join(reverse_str_x))
        if x > 2 ** 31 -1 or x < -2 ** 31:
            return 0
        else:
            return x
        
        # Solution 2
        # error for negative numbers
        # ans = 0
        # while(x != 0):
        #     if ans * 10 / 10 != ans:
        #         return 0
        #     ans = ans * 10 + x % 10
        #     x = x // 10
        # return ans