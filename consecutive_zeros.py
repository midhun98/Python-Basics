def consecutive_zeros(binary_string):
	count = 0
	max_count = 0
	for i in binary_string:
		if int(i) == 0:
			count += 1
			max_count = max(max_count, count)
		else:
			count = 0
	return max_count


number = "100011010000110"
print(consecutive_zeros(number))
