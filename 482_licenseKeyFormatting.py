class Solution:
	def licenseKeyFormatting(self, s: str, k: int) -> str:
		string = ""
		for i in s:
			if i.isalnum():
				string += i.upper()
		string = list(string)

		res = ""
		if len(string) % k == 0:
			counter = 0
			for i in string:
				res += i
				counter += 1
				if counter % k == 0:
					res += "-"
			res = res[:-1]
			return res

		if len(string) % k != 0:
			counter = 0
			for letter in string:
				res += letter
				counter += 1
				if counter == len(string) % k:
					res += "-"
					break

			out = ""
			counter = 0
			for i in string[len(string) % k :]:
				res += i
				counter += 1
				if counter % k == 0:
					res += "-"
			out = res + out
			return out[:-1]


ss = Solution()
s = "2-5g-3-J"
k = 2
print(ss.licenseKeyFormatting(s, k))
