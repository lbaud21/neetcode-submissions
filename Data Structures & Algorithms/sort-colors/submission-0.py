class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        buckets = [0] * 3

        for num in nums:
            buckets[num] +=1

        i = 0
        for bucket in range(len(buckets)):
            for _ in range(buckets[bucket]):
                nums[i] = bucket
                i += 1

        return nums
        