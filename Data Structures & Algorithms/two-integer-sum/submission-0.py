class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap={}
        n = len(nums)

        for i in range (0 ,n):
            curr_ind = i 
            compliment = target - nums[curr_ind]

            if compliment in hasmap:
                return [hasmap[compliment], curr_ind]
            
            hasmap[nums[curr_ind]] = curr_ind