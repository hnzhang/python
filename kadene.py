def max_subarray(arr:list)->list:
    if not arr:
        return None
    max_so_far = max_to_here = arr[0]
    start_index = 0
    end_index = 1
    start_index_so_far = 0
    end_index_so_far = 1

    for i in range(1, len(arr)):
        x = arr[i]
        max_candidate = x + max_to_here
        if x > max_candidate:
            start_index = i 
            max_to_here = x
        else:
            max_to_here = max_candidate
        end_index = i+1

        if max_to_here > max_so_far:
            start_index_so_far = start_index
            end_index_so_far = end_index
            max_so_far = max_to_here

        #max_to_here = max(x, max_to_here + x)
        #max_so_far = max(max_so_far, max_to_here)

    return (start_index_so_far, end_index_so_far, max_so_far)

def max_sum_rectangle(matrix):
    if not matrix or not matrix[0]:
        return None
    max_result = matrix[0][0]
    top= 0
    left = 0
    right = 1
    bottom = 1
    for col_step in range(1, len(matrix[0])):
        for i in range(len(matrix[0]) - col_step + 1):
            data = [0] * len(matrix)
            j = 0
            for row in matrix:
                data[j] = sum(row[i:col_step])
                j += 1
            result = max_subarray(data)
            if result[2] > max_result:
                max_result = result[2]
                top = result[0]
                bottom = result[1]
                left = i
                right = col_step

    return (max_result, left, top, right, bottom)


def test():
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    result = max_subarray(arr)
    if result:
        print(result)
    matrix = [
        [ 1,  2, -1, -4,-20],
        [-8, -3,  4,  2,  1],
        [ 3,  8, 10,  1,  3],
        [-4, -1,  1,  7, -6],
    ]
    print(max_sum_rectangle(matrix))

test()