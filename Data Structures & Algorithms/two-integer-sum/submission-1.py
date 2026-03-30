class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        naksha={}
        for index in range(len(nums)):
            if (target-nums[index]) in naksha.keys() :
                return [naksha[target-nums[index]], index]
            naksha[nums[index]]=index
        return [-1,-1]