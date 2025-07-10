from typing import List


class Solution:
	def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
		list1_dict = {}
		list2_dict = {}
		counter = 0
		for word in list1:
			list1_dict[word] = counter
			counter += 1
		counter = 0
		for word in list2:
			list2_dict[word] = counter
			counter += 1
		out = {}
		for key1, value1 in list1_dict.items():
			for key2, value2 in list2_dict.items():
				if key1 == key2:
					out[key1] = value1 + value2

		out_values = min(list(out.values()))
		res = []
		for key, value in out.items():
			if value == out_values:
				res.append(key)
		return res


ss = Solution()
list1 = ["happy", "sad", "good"]
list2 = ["sad", "happy", "good"]
ss.findRestaurant(list1, list2)
