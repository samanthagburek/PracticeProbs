class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroind = 0
        twoind = len(nums)-1
        curr = 0

        while curr <= twoind:
            if nums[curr] == 0:
                nums[curr], nums[zeroind] = nums[zeroind], nums[curr]
                zeroind += 1
                curr+=1
            elif nums[curr] == 2:
                nums[curr], nums[twoind] = nums[twoind], nums[curr]
                twoind -=1
            else:
                curr+=1
        return nums
