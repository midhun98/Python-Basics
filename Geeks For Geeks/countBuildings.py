"""
Given an array height representing the heights of buildings. You have to count the buildings that will see the sunrise (Assume the sun rises on the side of the array starting point).
Note: The height of the building should be strictly greater than the height of the buildings left in order to see the sun.

Input: height = [7, 4, 8, 2, 9]
Output: 3
Explanation: As 7 is the first element, it can see the sunrise. 4 can't see the sunrise as 7 is hiding it. 8 can see. 2 can't see the sunrise. 9 also can see
the sunrise.
"""


class Solution:
	def countBuildings(self, height):
		highest = height[0]
		out = 1
		for i in range(1, len(height)):
			if height[i] > highest:
				out += 1
				highest = height[i]
		return out


ss = Solution()
height = [7, 7, 8, 3, 2, 8, 9, 7]
print(ss.countBuildings(height))
