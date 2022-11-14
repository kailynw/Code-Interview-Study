#implement bubble sort and use various tests... you have until 6:26...go

def bubble_sort(array):
    ''' [53,563,24,2,-1,53] '''

    array_len = len(array)
    for i in range(array_len):
        last_unsorted_index = array_len - i - 1
        for j in range(last_unsorted_index):
            print("j: {}".format(j))
            if array[j] > array[j+1]:
                swap(j, j+1, array)

def bubble_sort_2(array):
    array_len= len(array)

    for i in range(array_len):
        last_unsorted_element = array_len-i-1
        print(last_unsorted_element)
        for j in range(last_unsorted_element):
            print("j: {}".format(j))
            if array[j]> array[j+1]:
                swap(j, j+1, array)

def swap(j, j_plus_one, array):
    if j == j_plus_one:
        return
    else:
        temp = array[j]
        array[j] = array[j_plus_one]
        array[j_plus_one] = temp

if __name__ =="__main__":

    #full array
    array=[-94,29,4,-1,52,-582,5,-95]
    bubble_sort_2(array)
    print(array)

    # #empty array
    # array=[]
    # bubble_sort(array)
    # print(array)


    # #one element array
    # array=[5]
    # bubble_sort(array)
    # print(array)

    # #two element array
    # array=[42,-4]
    # bubble_sort(array)
    # print(array)




