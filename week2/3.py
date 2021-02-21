class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for i in list(set(nums)):
            count = nums.count(i)
            result += count*(count-1)/2
        return int(result)    