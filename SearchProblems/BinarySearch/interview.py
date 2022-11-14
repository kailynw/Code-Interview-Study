def binary_search(array:list, target:int):
    left = 0
    right = len(array)-1

    while left<=right:
        pivot = left + (right-left)//2
        if target == array[pivot]:
            return pivot
        elif target > array[pivot]:
            left = pivot + 1
        else:
            right = pivot - 1
    return -1

if __name__ == "__main__":
    array = [-1,3,53,46,424,538]
    searched_index= binary_search(array, 538)
    print(searched_index)