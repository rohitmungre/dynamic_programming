class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lis = s.split()
        newlis = []
        for item in lis:
            newlis = [str(item)] + newlis
        return ' '.join(newlis)        
