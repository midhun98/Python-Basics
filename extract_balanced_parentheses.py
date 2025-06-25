def extract_balanced_parantheses(s):
    result = []  # To store the balanced groups
    count = 0  # To track the number of open parentheses
    group = ""  # To accumulate characters for each group

    for char in s:
        group += char  # Add the current character to the current group

        # Update the count based on the character
        if char == "(":
            count += 1
        if char == ")":
            count -= 1

        # If count is 0, we have a balanced group
        if count == 0:
            result.append(group)  # Add the current balanced group to the result
            group = ""  # Reset the group for the next balanced group

    return result


x = "(())((()))(())"
out = extract_balanced_parantheses(x)
print(out)  # Output: ['(())', '((()))', '(())']
