




def minimum_ocurrence(string1):
    if not string1:
        return ""

    char_counts = {}

    for char in string1:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    min_occurrence = min(char_counts.values())

    for char in string1:
        if char_counts[char] == min_occurrence:
            return char
    return None













print(minimum_ocurrence("asdsaaa"))