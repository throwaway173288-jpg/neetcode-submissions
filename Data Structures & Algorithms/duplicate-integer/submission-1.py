class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash=set(nums)
        return len(hash)<len(nums)
