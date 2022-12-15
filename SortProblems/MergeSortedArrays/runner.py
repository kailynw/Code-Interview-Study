def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    i, j = m-1, n-1
    for right in range(m+n-1, -1, -1):
        if j < 0:
            break
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[right] = nums1[i]
            i -= 1
        else:
            nums1[right] = nums2[j]
            j -= 1

if __name__ == "__main__":
    list1 = [2,0]
    list2 = [1]
    list_1_len = len(list1) - len(list2)
    merge(list1,list_1_len, list2, len(list2))
    print(list1)