## For ordering n elements, we need at least n-1 operations. 
[Leetcode 1464: Maximum Product of Two Elements in an array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)

My solution is at [here](https://github.com/alvinctk/learn/blob/main/leetcode/lc_1464_max_product_two_elements_in_array.py)

For example: select two maximum numbers in array of unsorted numbers.

`nums` = Unsorted array of integers 

Determine first two indexed elements in the unsorted array such that `upper` >= `lower`. 

Slide the window to include one element at each iteration. 

At each iteration, we have three elements to consider for ordering, namely,
`upper`, `lower`, and `nums[i]` 

We know that `upper` >= `lower`. 

To determine the ordering of a <= b <= c, only 2 comparison is required

To check the upper bound, if `nums[i]` is the upper bound.

To check the lower bound, if `nums[i]` is the lower bound. 

```python3
def max2(upper, lower):
    return (upper, lower) if upper >= lower else (lower, upper)

i, n = 2, len(nums)
upper, lower = max2(nums[0], nums[1])

while i < n:
    a, _ = max2(upper, nums[i])
    b, _ = max2(nums[i], lower)

    if a == nums[i]:
        # since nums[i] >= upper >= lower
        upper, lower = nums[i], upper
    elif b == nums[i]:
        # since upper >= nums[i] >= lower
        upper, lower = upper, nums[i]
    # not need since upper >= lower >= nums[i]

    i += 1
```
