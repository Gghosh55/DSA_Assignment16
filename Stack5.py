class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


def reverse_number(number):
    stack = Stack()

    for digit in str(number):
        stack.push(digit)

    reversed_number = ''

    while not stack.is_empty():
        reversed_number += stack.pop()

    return int(reversed_number)

number = 12345
reversed_number = reverse_number(number)
print("Original number:", number)
print("Reversed number:", reversed_number)
