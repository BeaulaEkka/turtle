
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        result = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1

        result.reverse()  # Because we're adding larger squares first
        return result


solution = Solution()
nums = [-4, -1, 0, 3, 10]
twoPointers = solution.sortedSquares(nums)
print(twoPointers)  # Output: [0, 1, 9, 16, 100]
