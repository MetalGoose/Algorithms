def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
    return None


def binary_search_reverse(arr, item):
    if len(arr) == 0:
        return False
    else:
        midpoint = len(arr) // 2
        print(arr[midpoint])
        if arr[midpoint] == item:
            return True
        else:
            if item < arr[midpoint]:
                print(arr[:midpoint])
                return binary_search_reverse(arr[:midpoint], item)
            else:
                print(arr[midpoint+1:])
                return binary_search_reverse(arr[midpoint+1:], item)


test_list = [1,2,5,7,55,77,82,126,441,999,6883]

print(binary_search_reverse(arr=test_list, item=555))