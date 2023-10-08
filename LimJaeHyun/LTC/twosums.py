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