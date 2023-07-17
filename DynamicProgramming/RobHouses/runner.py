def rob_houses(nums: list):
    house1, house2 = 0, 0

    for n in nums:
        temp = max(house2, n + house1)
        house1 = house2
        house2 = temp
    return house2

def rob_houses_mine(nums: list):
    
    len_nums = len(nums)      
    if len_nums == 2:
        return max(nums[0], nums[1])
    if len_nums == 1:
        return nums[0]

    house1 = nums[0]
    house2 = nums[1]

    for i in range(2, len(nums)):
        temp = max(house2, nums[i] + house1)
        house1 = house2
        house2 = temp
    
    return house2

def rob(nums):
    
    last, now = 0, 0
    
    for i in nums: last, now = now, max(last + i, now)
            
    return now

if __name__ == "__main__":
    data = [2, 1 , 1, 2]
    print(f"Mine: {rob_houses_mine(data)}")
    print(f"Neetcode: {rob_houses_mine(data)}")
    print(f"some dude: {rob_houses_mine(data)}")

