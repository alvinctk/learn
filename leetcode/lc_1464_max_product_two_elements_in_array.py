class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        def max2(upper, lower):
            return (upper, lower) if upper >= lower else (lower, upper)  

        i, n = 2, len(nums)
        upper, lower = max2(nums[0], nums[1])
        
        while i < n:
            a, b = max2(upper, nums[i])
            c, d = max2(nums[i], lower) 
            
            if b == upper:
                # since nums[i] >= upper >= lower 
                upper, lower = nums[i], upper
            elif c == nums[i]:
                # since upper >= nums[i] >= lower
                upper, lower = upper, nums[i]
            # not need since upper >= lower >= nums[i]
            
            i += 1 
        upper -= 1
        lower -= 1 
        return upper * lower
            
        
