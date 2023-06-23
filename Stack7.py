def count_remaining_words(sequence):
    stack = []

    for word in sequence:
        if len(stack) > 0 and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)

    return len(stack)

sequence = ["ab", "aa", "aa", "bcd", "ab"]
remaining_words = count_remaining_words(sequence)
print("Number of words left:", remaining_words)
