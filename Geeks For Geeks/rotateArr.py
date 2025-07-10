# User function Template for python3

class Solution:
	def rotateArr(self, arr, d):
		n = len(arr)
		d %= n
		arr = self.reverse(0, d - 1, arr)
		arr = self.reverse(d, n - 1, arr)
		arr = self.reverse(0, n - 1, arr)
		print(arr)

	def reverse(self, left, right, arr):
		while left < right:
			arr[left], arr[right] = arr[right], arr[left]
			left += 1
			right -= 1
		return arr


ss = Solution()
arr = [1, 2, 3, 4, 5]
d = 2
print(ss.rotateArr(arr, d))
