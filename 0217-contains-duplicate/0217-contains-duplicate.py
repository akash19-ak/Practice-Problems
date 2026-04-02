class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        re=set()
        for no in nums:
            if no in re:
                return True

               
            else:
                re.add(no)

        return False