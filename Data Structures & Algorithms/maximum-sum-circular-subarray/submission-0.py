class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0
        for num in nums:
            curMax=max(curMax+num,num)
            curMin=min(curMin+num,num)
            total+=num
            globMax=max(globMax,curMax)
            globMin=min(globMin,curMin)
        circularMax=total-globMin
        if globMax>0:
            return max(globMax,circularMax)
        return globMax
        
