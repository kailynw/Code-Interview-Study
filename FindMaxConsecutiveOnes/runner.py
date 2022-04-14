def findMaxConsecutiveOnes(nums: List[int]) -> int:
    count=0
    max_count= 0
    for num in nums:
        ''' if 0, then find max between count and max count and set that equal to max count, reset count'''
        if num ==0:
            max_count = max(count, max_count)
            count=0
        else: 
            ''' If 1, then increment count'''
            count+=1
    return max(count, max_count)


if __name__ == "__main__":
    findMaxConsecutiveOnes([])
