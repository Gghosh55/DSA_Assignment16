def delete_middle(stack, k):

    if len(stack) == 0 or k == 0:
        stack.pop()
        return


    temp = stack.pop()
    delete_middle(stack, k - 1)


    stack.append(temp)


def delete_middle_element(stack):
    size = len(stack)
    k = size // 2 + 1

    delete_middle(stack, k)



stack = [1, 2, 3, 4, 5]
print("Input stack:", stack)
delete_middle_element(stack)
print("Modified stack:", stack)

stack = [1, 2, 3, 4, 5, 6]
print("Input stack:", stack)
delete_middle_element(stack)
print("Modified stack:", stack)
