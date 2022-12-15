def intersection(nums1: list, nums2:list):
    shortest_list = []
    longest_list = []
    intersect_list = []
    
    if len(nums1)>len(nums2):
        longest_list = nums1
        shortest_list = nums2
    else:
        longest_list = nums2
        shortest_list = nums1

    count_map = counter(longest_list)
   
    for num in shortest_list:
        if num in longest_list and count_map[num] > 0:
            intersect_list.append(num)
            count_map[num] = count_map[num]-1
    return intersect_list



def counter(nums: list):
    count_map = {}

    for num in nums:
        if num in count_map:
            count_map[num] = count_map[num] + 1
        else:
            count_map[num] = 1
    return count_map

if __name__ == "__main__":
    list1 = [1,2,3,4,5,8,10,2,3,20]
    list2 = [5,2,90]

    intersect_list = intersection(list1, list2)
    print(intersect_list)