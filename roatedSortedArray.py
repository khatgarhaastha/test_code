class solution:
    
    
    def __init__(self, nums: list[int], target: int):
        self.nums = nums
        self.target = target
        
        
    def find_pivot(self, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2 
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid -1
        return left
    
    def binary_search(self,left_boundary, right_boundary, tar):
        array = self.nums 
        while left_boundary <= right_boundary:
            middle = left_boundary + (right_boundary - left_boundary)//2
            if tar == array[middle]:
                return middle
            elif tar < array[middle]:
                right_boundary = middle -1 
            else :
                left_boundary = middle + 1
        return -1
    
    def find_target_index(self, nums, target):
        pivot = self.find_pivot(nums)
        if target == nums[pivot]:
            return pivot
        elif nums[0]<= target < nums[pivot-1]:
            return self.binary_search(0, pivot, target)
        elif nums[pivot] < target <= nums[-1]:
            return self.binary_search(pivot, len(nums)-1, target)
        
        
sol = solution([7,8,9,11,13,15,0,1,2,4,5], 10)
index_of_target = sol.find_target_index(sol.nums, sol.target)
print(f"the index of the target is: {index_of_target}")