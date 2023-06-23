from collections import Counter

def find_nearest_greater_frequency(arr):
    frequency = Counter(arr)
    n = len(arr)
    answers = []

    for i in range(n):
        current = arr[i]
        answer = -1

        for j in range(i + 1, n):
            if frequency[arr[j]] > frequency[current]:
                answer = arr[j]
                break

        answers.append(answer)

    return answers
arr = [1, 1, 2, 3, 4, 2, 1]

print(find_nearest_greater_frequency(arr))
