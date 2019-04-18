def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    print(pivot)
    less = [i for i in array[1:] if i <= pivot]
    print(less,'less')
    greater = [i for i in array[1:] if i > pivot]
    print(greater,'greater')
    return quick_sort(less) + [pivot] + quick_sort(greater)

test_list = [1,2,5,7,2,0,-1,33,3,4,441,999,555,6883]

print(quick_sort(test_list))