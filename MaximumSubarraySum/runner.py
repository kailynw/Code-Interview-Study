import math
def maxSubArray(nums):
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                print(f"Sub-array starting at: {i} | {nums[i:j]} ")
                max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray

if __name__ == "__main__":
    array = [-2,1,-3,4,-1,2,1,-5,4]
    ans = maxSubArray(array)