'''

Question:
Given two integer arrays, return their intersection.
Note: the intersection is the set of elements that are common to both arrays.
Ex: Given the following arrays:
nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []

'''
def listIntersection(list1, list2):
    list1_set = set()
    for i in list1:
        if i in list2:
            list1_set.add(int(i))
    return list(list1_set)

list1 = list(input())
list2 = list(input())
print("The intersection of both the arrays: ", listIntersection(list1,list2))