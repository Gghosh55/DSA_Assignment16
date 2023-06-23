def check_queue(arr):
    stack = []
    other_queue = []

    for num in arr:
        while len(stack) > 0 and num > stack[-1]:
            other_queue.append(stack.pop())

        if len(other_queue) > 0 and num < other_queue[0]:
            return False

        stack.append(num)

    while len(stack) > 0:
        other_queue.append(stack.pop())

    for i in range(1, len(other_queue)):
        if other_queue[i] < other_queue[i - 1]:
            return False

    return True


queue = [5, 1, 2, 6, 3, 4]
result = check_queue(queue)
print(result)
