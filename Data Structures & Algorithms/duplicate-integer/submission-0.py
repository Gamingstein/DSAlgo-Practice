class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort();
        for index in range(len(nums)-1):
            if nums[index] ^ nums[index+1] == 0:
                return True
        return False