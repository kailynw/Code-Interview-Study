from typing import List


def removeDuplicates(nums: List[int]):
    if len(nums) < 2: return len(nums)
    slow, fast = 2, 2

    while fast < len(nums):
        if nums[slow - 2] != nums[fast]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow


if __name__ == "__main__":
    array = [1,2,2,2,3,4,5,5,5,5,5,6,6]
    removeDuplicates(array)
    print(array)


    # First iter
    slow = fast = 2

    array[slow] = 2
    array[fast] = 2
    slow = 3
    fast = 3
    array = [1,2,2,2,3,4,5,5,5,5,5,6,6]

    # Second iter
    slow = fast = 3

    array[slow] = 2
    array[fast] = 2
    slow = 3
    fast = 4
    array = [1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5, 6, 6]

    # Third iter
    slow, fast = 3, 4

    array[slow] = 3
    array[fast] = 3
    slow = 4
    fast = 5
    array = [1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5, 6, 6]

