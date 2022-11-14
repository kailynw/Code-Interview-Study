
'''Bubble sort implementation 1 - Loops through array with two pointers that start at the beginning.
   Loop through comparing values (array[i] > array[j]) checking if one value is greater than the other to swap
'''
def bubble_sort_imp_1(array):
    array_len = len(array)
    print(array_len)

    for i in range(array_len):
        for j in range(i+1,array_len):
            print("Where am I? i={} [Element: {} ]| j={} Element: {}]".format(i, j, array[i], array[j]))
            if (array[i]> array[j]):
                print("Swapping values: {} | {}".format(array[i], array[j]))
                _swap(i, j, array)

'''Bubble sort implementation 2 - Loops through array with one pointer that starts at the beginning of the array and one pointer that start at the end.
   Loop through comparing values (array[i] > array[j]) checking if one value is greater than the other to swap
'''
def bubble_sort_imp_2(array):
    print("hi")
    array_len = len(array)

    for last_unsorted_index in range(array_len, 0, -1):
        print(last_unsorted_index)
        for i in range(last_unsorted_index):
            if array[i] > array[i+1]:
                _swap(i, i+1, array)


def bubble_sort_imp_3(array):
    array_len = len(array)

    for i in range(array_len):
        last_unsorted_index = array_len-i-1
        for j in range (0, last_unsorted_index):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] #swap

def _swap(i, j, array):
    if (i==j):
        return

    temp= array[i]
    array[i]= array[j]
    array[j]=temp

if __name__ =="__main__":
        array = [4,2,56,-56,1,0,25,7]
        # bubble_sort_imp_1(array)
        bubble_sort_imp_3(array)
        print(array)