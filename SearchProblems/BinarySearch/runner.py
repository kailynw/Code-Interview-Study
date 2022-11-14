def binary_search(array:list, target:int ):
    left = 0
    right = len(array)-1

    while left <=right:
        pivot = left + (right-left)//2
        if (target == array[pivot]):
            return pivot
        elif (target <= array[pivot]):
            right = pivot-1
        else:
            left = pivot+1
    return -1

if __name__=="__main__":
    array = [1,4,6,73,314,795]
    search_index = binary_search(array, 314)
    print(search_index)