# Return True if the list contains a duplicate, else False.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict: return True
            else:
                my_dict[nums[i]] = 1
        return False