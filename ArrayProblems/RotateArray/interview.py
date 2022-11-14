def rotate_array(array:list, rotation_times:int):
    rotation_times%=len(array)

    for i in range(rotation_times):
        previous = array[-1]
        for i in range(len(array)):
            previous, array[i] = array[i], previous
    print(array)
if __name__ == "__main__":
    array = [1,2,3,4,5,6]
    rotate_array(array, 6)

