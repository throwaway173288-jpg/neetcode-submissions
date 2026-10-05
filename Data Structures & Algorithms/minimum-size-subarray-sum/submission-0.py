class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curSum = 0
        minSubArray = float("inf")  # 1. Start with infinity!
        
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minSubArray = min(minSubArray, r - l + 1)
                curSum -= nums[l]
                l += 1
        return minSubArray if minSubArray != float("inf") else 0