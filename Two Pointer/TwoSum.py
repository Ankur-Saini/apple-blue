

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        index = {}
        for i in range(n):
            if nums[i] not in index:
                index[nums[i]] = [i]
            else:
                index[nums[i]].append(i)
        nums.sort()
        i = 0
        j = n - 1
        sum = 0
        while i <= j:
            sum = nums[i] + nums[j]
            if sum == target:
                if nums[i] == nums[j]:
                    return [index[nums[i]][0], index[nums[i]][1]]
                return [index[nums[i]][0], index[nums[j]][0]]
            elif sum > target:
                j -= 1
            else:
                i += 1
