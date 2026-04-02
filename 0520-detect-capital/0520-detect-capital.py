class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        upp_count = 0
        for letter in word:
            if letter.isupper():
                upp_count+=1
        if upp_count==0:
                return True
        if upp_count==len(word):
                return True
        if upp_count==1 and word[0].isupper():
                return True
        else:
                return False    
