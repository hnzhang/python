'''
a module to demo all kinds of sorting algorithms
'''
def heapify_max(arr, size, index):
    left = index *2 +1
    right = index *2 +2
    largest = index
    if left < size and arr[left] > arr[index]:
        largest = left
    if right < size and arr[right] > arr[index]:
        largest = right
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify_max(arr, size, largest)

def heap_sort(arr):
    size = len(arr)
    for i in range(size-1, -1, -1):
        heapify_max(arr, size, i)
    for i in range(size-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_max(arr, i, 0)

def insertion_sort(data_list):
    '''
    use insertion sort to sort given list
    '''
    if not data_list:
        return
    for index in range(1, len(data_list)):
        position = index
        current_value = data_list[index]

        while position > 0 and data_list[position - 1] > current_value:
            data_list[position] = data_list[position-1]
            position -= 1

        if position != index:
            data_list[position] = current_value

def merge_helper(left, right):
    '''
    merge left and right lists into one list. left and right are sorted
    '''
    index_left = 0
    index_right = 0
    merged_result = []
    while index_left < len(left) and index_right < len(right):
        if left[index_left] < right[index_right]:
            merged_result.append(left[index_left])
            index_left += 1
        else:
            merged_result.append(right[index_right])
            index_right += 1
    while index_left < len(left):
        merged_result.append(left[index_left])
        index_left += 1
    while index_right < len(right):
        merged_result.append(right[index_right])
        index_right += 1
    return merged_result

def merge_sort(data_list):
    '''
    sort data using merge sort
    '''
    if len(data_list) > 1:
        mid = len(data_list)//2
        left = merge_sort(data_list[:mid])
        right = merge_sort(data_list[mid:])
        return merge_helper(left, right)
    else:
        return data_list

def main():
    '''
    main function for testing
    '''
    test_data_insertion_sort = [10, 4, 7, 1, 20, 8, 100, 23, 45, 12]
    print("before insertion sort:", test_data_insertion_sort)
    insertion_sort(test_data_insertion_sort)
    print("after insertion sort:", test_data_insertion_sort)

    test_data_for_merge_sort = [10, 4, 7, 1, 20, 8, 100, 23, 45, 12]
    print("before merge sort", test_data_for_merge_sort)
    merged_result = merge_sort(test_data_for_merge_sort)
    print("after merge sort", merged_result)
    test_data_for_heap_sort = [10, 4, 7, 1, 20, 8, 100, 23, 45, 12]
    print("before heap_sort", test_data_for_heap_sort)
    heap_sort(test_data_for_heap_sort)
    print("after heap sort", test_data_for_heap_sort)

main()

