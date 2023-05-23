def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    
    for i, a in enumerate(nums):
        if i > 0 and nums[i - 1] == a:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            sum = a + nums[l] + nums[r]
            if sum == 0:
                res.append([a, nums[l], nums[r]])                    
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
            elif sum > 0:
                r -= 1
            else:
                l += 1

    return res