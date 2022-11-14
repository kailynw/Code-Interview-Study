def bubble_sort(array:list):
    #[34,532,53,-13,53]
    array_length = len(array)
    for i in reversed(range(array_length)):
        last_unsorted_index = i
        for j in range(last_unsorted_index):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
if __name__ == "__main__":
    array = [34,532,53,-13,98]
    sorted_array = bubble_sort(array)
    print(sorted_array)