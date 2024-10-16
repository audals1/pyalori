def backtrack(nums):
    stack = [(0, nums[:])]
    result = []

    while stack:
        start, current = stack.pop()
        if start == len(current):
            result.append(current[:])
        else:
            for i in range(start, len(current)):
                current[start], current[i] = current[i], current[start]
                stack.append((start + 1, current[:]))
                current[start], current[i] = current[i], current[start]

    return result

nums = [1, 2, 3]
result = backtrack(nums)
print(result)

