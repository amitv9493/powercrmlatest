from functools import reduce

from typing import List


def finalValueAfterOperations(operations: List[str]) -> int:
    return reduce(lambda a, b: a + (1 if b[1] == "+" else -1), operations, 0)


print(finalValueAfterOperations(["--X", "X++", "X++"]))

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(reduce)


def dec(func):
    def inner(*args, **kwargs):
        print("running inner()")
        return func(*args, **kwargs)

    return inner


ids = ["id1", "id2", "id30", "id3", "id22", "id100"]

print(sorted(ids, key=lambda x: int(x[2:]), reverse=True))


def twoSum(nums: List[int], target: int) -> List[int]:
    numMap = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i

    return []


print(twoSum(nums=[3, 3], target=6))
