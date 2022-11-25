from structures.Arrays import Array

# Ej 1
# Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


def ejercicio1(nums, target):
    size = len(nums)
    for i in range(size):
        for j in range(size):
            if nums[i] + nums[j] == target:
                return [i, j]
        return []

# Ej 2
#Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


def ejercicio2(nums):
    size = len(nums)
    insertIndex = 1
    for i in range(1, size):
        if nums[i - 1] != nums[i]:
            nums[insertIndex] = nums[i]
            insertIndex = insertIndex + 1

    # Eliminamos el resto
    for i in range(insertIndex, size):
        nums[i] = None
    return insertIndex, nums

# Ej 3
# Input: nums = [1,3,5,6], target = 5
#Output: 2


def ejercicio3_v1(nums, target):
    size = len(target)
    for i in range(size):
        if target <= nums[i]:
            return i


def ejercicio3_v2(nums, target):
    left = 0
    right = len(nums) - 1
    while (left <= right):
        mid = int((left + right) / 2)
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1
    return right + 1

# Ej 4
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


def ejercicio4(nums1, m, nums2, n):
    i = 0  # iterador para nums1
    j = 0  # iterador para nums2
    while (j < n and i < m + n):
        if nums2[j] < nums1[i]:
            for k in range(m + j, i, -1):
                nums1[k] = nums1[k-1]
            nums1[i] = nums2[j]
            j += 1

        if m + j == i:
            nums1[i] = nums2[j]
            j += 1

        i += 1
    return nums1
