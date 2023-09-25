class Solution(object):
	def twoSum(self, nums, target):
		result = []
		if len(nums) == 2:
			return [0, 1]
		else:
			for i in range(len(nums)):
				for k in range(i+1, len(nums)):
					if nums[i] + nums[k] == target:
						return [i, k]
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""

""" #optimized Code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []
"""