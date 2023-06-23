def sort_stack(stack):
    temp_stack = []

    while stack:
        if not temp_stack or stack[-1] >= temp_stack[-1]:
            temp_stack.append(stack.pop())
        else:
            temp = stack.pop()
            while temp_stack and temp < temp_stack[-1]:
                stack.append(temp_stack.pop())
            stack.append(temp)

    while temp_stack:
        stack.append(temp_stack.pop())

    while stack:
        print(stack.pop(), end=" ")


stack = [34, 3, 31, 98, 92, 23]
print("Input: ", stack)
print("Sorted stack: ", end="")
sort_stack(stack)
print()

stack = [3, 5, 1, 4, 2, 8]
print("Input: ", stack)
print("Sorted stack: ", end="")
sort_stack(stack)
print()
