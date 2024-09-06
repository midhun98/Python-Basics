from itertools import combinations

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
k = 72


def find_combinations(li, k):
    result = []
    for r in range(1, len(li) + 1):
        for combo in combinations(li, r):
            print(combo)
            if prod(combo) == k:
                result.append(combo)
    return result


def prod(iterable):
    result = 1
    for x in iterable:
        result *= x
    return result


combinations_that_multiply_to_k = find_combinations(li, k)
print(combinations_that_multiply_to_k)
