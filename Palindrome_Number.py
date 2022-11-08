class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        x_length = len(str_x)
        if x_length == 1:
            return True
        if x_length == 2:
            return str_x[0] == str_x[-1]
        else:
            if str_x[0] == str_x[-1]:
                return self.isPalindrome(str_x[1:-1])
            else:
                return False
