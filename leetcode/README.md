## For ordering n elements, we need at least n-1 operations. 

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
```
