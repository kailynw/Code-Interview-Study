def rotate_array(array, rotation_times) -> None:
        # speed up the rotation
        rotation_times %= len(array)

        for i in range(rotation_times):
            previous = array[-1]
            for j in range(len(array)):
                array[j], previous = previous, array[j]

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7]
    rotate_array(array, 3)
    
    # rotate_amount = 14
    # array_length = 5

    # rotate_amount= rotate_amount % array_length 
    # print(rotate_amount)