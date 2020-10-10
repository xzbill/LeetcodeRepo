class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        notEnd = True
        common_pre = ''
        idx = 0
        # strs should not be empty
        if(len(strs) <= 0):
            return common_pre
        while(notEnd):
            ichar = ''
            for elem in range(len(strs)):
                # each element should not be empty
                if idx >= len(strs[elem]):
                    return common_pre
                if elem == 0:
                    ichar = strs[elem][idx]
                else:
                    if ichar != strs[elem][idx]:
                        return common_pre
            # finish idx-th loop
            common_pre += ichar
            idx += 1