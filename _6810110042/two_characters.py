from itertools import combinations


def alternate(s):
    unique_chars = set(s)
    max_length = 0

    for char1, char2 in combinations(unique_chars, 2):
        filtered = [c for c in s if c == char1 or c == char2]

        is_alternating = True
        for i in range(1, len(filtered)):
            if filtered[i] == filtered[i - 1]:
                is_alternating = False
                break

        if is_alternating:
            max_length = max(max_length, len(filtered))

    return max_length
