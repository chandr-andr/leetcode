class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [ int(val) for val in str(int("".join(map(str, digits))) + 1) ]
