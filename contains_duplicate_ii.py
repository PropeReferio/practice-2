#Given an array of integers and an integer k, find out whether there are two 
# distinct indices i and j in the array such that nums[i] = nums[j] and the 
# absolute difference between i and j is at most k.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) == 1: return False
        # The difference between the matching indices must be <= k
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]].append(i)
            else:
                my_dict[nums[i]] = [i]
        # Loop over each value, which are lists of indices, and check if
        # any difference between indices is <= k.
        for value in my_dict.values():
            if len(value) >= 2:
                for i in range(len(value)-1):
                    if (value[i+1] - value[i]) <= k:
                        return True
        return False