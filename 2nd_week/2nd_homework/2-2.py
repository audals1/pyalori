def find_longest_substr(s):
    hashtable = {}
    start = 0
    max_length = 0

    for index, char in enumerate(s):
        if char in hashtable and hashtable[char] >= start:
            start = hashtable[char] + 1

        hashtable[char] = index
        max_length = max(max_length, index - start + 1)

    return max_length

input = "aabca"
result = find_longest_substr(input)
print(result)