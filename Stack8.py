def max_absolute_difference(arr):
    n = len(arr)
    left_smaller = [0] * n
    right_smaller = [0] * n
    stack = []


    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left_smaller[i] = stack[-1]
        stack.append(i)

    stack.clear()


    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right_smaller[i] = stack[-1]
        stack.append(i)

    max_difference = 0


    for i in range(n):
        difference = abs(left_smaller[i] - right_smaller[i])
        max_difference = max(max_difference, difference)

    return max_difference


# Example usage
arr = [2, 1, 8]

print("Maximum absolute difference:", max_absolute_difference(arr))
