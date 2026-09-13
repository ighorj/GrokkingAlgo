def binary_search(element, arr)

high = len(arr) - 1
low = 0

while low <= high:
    mid = (high + low) // 2
    if arr[mid] = element:
        return mid
    if arr[mid] < element:
        low = mid + 1
    elif arr[mid] > element:
        high = mid - 1
return None
