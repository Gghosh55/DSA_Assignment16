from queue import Queue


def reverse_k_elements(queue, k):
    if queue.empty() or k <= 0 or k > queue.qsize():
        return

    stack = []


    for _ in range(k):
        stack.append(queue.get())


    while stack:
        queue.put(stack.pop())


    for _ in range(queue.qsize() - k):
        queue.put(queue.get())


queue = Queue()
elements = [1, 2, 3, 4, 5, 6, 7]
for element in elements:
    queue.put(element)

k = 4
reverse_k_elements(queue, k)

for _ in range(k):
    print(queue.get())
