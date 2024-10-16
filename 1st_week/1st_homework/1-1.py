import string

def ispalindrome():
    word = input()
    middle_index = len(word) // 2
    if len(word) % 2 != 0:
        left = word[:middle_index]
        right = word[middle_index + 1:]

    else:
        left = word[:middle_index]
        right = word[middle_index:]

    print(left == right[::-1])

ispalindrome()