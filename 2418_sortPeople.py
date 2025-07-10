from typing import List


class Solution:
	def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
		# Alternate Solution Start
		height_to_name = {}
		for h, n in zip(heights, names):
			height_to_name[h] = n
		print("height_to_name", height_to_name)
		res = []
		rev_heights = list(reversed(sorted(heights)))
		print("rev_heights", rev_heights)
		for height in rev_heights:
			res.append(height_to_name[height])
		print("res", res)
		# Alternate Solution End

		height_dict = {}
		for index, value in enumerate(heights):
			height_dict[value] = index

		myKeys = heights
		myKeys.sort()
		sorted_dict = {}

		for i in myKeys:
			sorted_dict[i] = height_dict[i]

		out = []
		for key, value in sorted_dict.items():
			out.append(names[value])
		return out[::-1]


ss = Solution()
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
print(ss.sortPeople(names, heights))
