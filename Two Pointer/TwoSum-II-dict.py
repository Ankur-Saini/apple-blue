
# Dictionary approach
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(numbers):
            if target - num in num_dict:
                return [num_dict[target - num] + 1, i + 1]
            num_dict[num] = i


