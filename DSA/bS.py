# arr = { 2,3,45,5,7,9,6}

# def binary_search(item , list):
#     min = 0
#     max = len(list) - 1
    
#     while min <= max:
#         mid = round((min + max ) / 2)
#         if mid == item:
#             return mid
#         if mid > item:
#             max = mid - 1
#         else:
#              min = mid + 1
#     return None

# print(binary_search(9, arr))



# Binary Search in python


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")