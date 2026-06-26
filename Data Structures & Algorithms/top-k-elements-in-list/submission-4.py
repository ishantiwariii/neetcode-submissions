class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]

        freq_map = {}

        for i in range (0,n):
            if nums[i] in freq_map:
                freq_map[nums[i]] += 1 
            else :
                freq_map[nums[i]] = 1

        for num,count in freq_map.items():
            bucket[count].append(num)

        ans = []

        for i in range (n , -1 , -1):
            for num in bucket[i]:
                ans.append(num)

            if len(ans) == k:
                return ans