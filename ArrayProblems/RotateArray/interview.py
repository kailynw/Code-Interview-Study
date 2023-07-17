def rotate_array_on2(array:list, rotation_times:int):
    rotation_times%=len(array)

    for i in range(rotation_times):
        previous = array[-1]
        for i in range(len(array)):
            previous, array[i] = array[i], previous
    print(array)

def rotate_array_on(nums: list, rotation_times: int):
    for i in range(rotation_times):
        n = nums[len(nums) - 1]
        nums.pop()
        nums.insert(0, n)
if __name__ == "__main__":
    array = [1,2,3,4,5,6]
    rotate_array_on(array, 3)


