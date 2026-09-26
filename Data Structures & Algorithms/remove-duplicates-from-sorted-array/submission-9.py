class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        c = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[c] = nums[i]
                c += 1
        return c

        # [1 ,1 ,1 ,2 ,3 ,4, 4]

        # [1 , 2 , 3 , 4 , 3 ,4, 4]

        # c = 1 , i = 0
        # c = 1 , i = 1
        # c = 1 , i = 2
        # c = 2 , i = 3
        # c = 3 , i = 4

        

        


        