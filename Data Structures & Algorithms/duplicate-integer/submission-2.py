class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr=[]
        for i in nums:
            if i in arr:
                return True
            else:
                arr.append(i);
        return False
