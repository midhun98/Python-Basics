l1 = [1, 2, 4]
l2 = [1, 3, 4]

out = []
i = 0
j = 0

while i < len(l1) and j < len(l2):
	if l1[i] < l2[j]:
		out.append(l1[i])
		i += 1
	else:
		out.append(l2[j])
		j += 1

# Add remaining elements
while i < len(l1):
	out.append(l1[i])
	i += 1

while j < len(l2):
	out.append(l2[j])
	j += 1

print(out)  # Output: [1, 1, 2, 3, 4, 4]
