# My first recursive option:

class Solution:
    def checkAll(self, curSum: int, sliced: List[int], routes: List[int]):
        if len(sliced) == 0: routes.append(curSum)
        if len(sliced) <= 2:
            for i in range(len(sliced)):
                routes.append(curSum + sliced[i])
        if len(sliced) > 2:
            for i in range(len(sliced)-2):
                self.checkAll(curSum + sliced[i], sliced[i+2:], routes)
            routes.append(curSum+sliced[-1])
            routes.append(curSum+sliced[-2])
        
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        routes = []
        self.checkAll(nums[0], nums[2:], routes)
        self.checkAll(nums[1], nums[3:], routes)
        return max(routes) # Maybe just keep track of max on our own, rather than
    # keep a list and use the max function

# Algorithm called DP?:
class Solution2:
		def rob(self, nums: List[int]) -> int:
        rob = 0
        skip = 0
        for n in nums:
            _rob, _skip = rob, skip
            skip = max(_rob, _skip)
            rob = _skip + n
        return max(rob, skip)