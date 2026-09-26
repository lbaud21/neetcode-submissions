class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        for i in nums:
            if i == val:
                continue
            temp.append(i)
        for index, item in enumerate(temp):
            nums[index] = item

        return len(temp)
        