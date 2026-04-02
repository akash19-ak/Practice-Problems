class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        store=""
        for letter in s:
            if letter.isalnum():
                store+=letter.lower()
        
        rev=store[::-1]
        if rev==store:
            return True
        else:
            return False