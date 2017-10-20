def rotate_image(image_matrix):
    if not image_matrix:
        return image_matrix
    
    size = len(image_matrix)
    print("size", size)
    for row in range(0, size - 1):
        for col in range(0, size - row - 1):
            tmp = image_matrix[row][col]
            mapped_row = size - col -1
            mapped_col = size - row -1
            image_matrix[row][col] = image_matrix[mapped_row][mapped_col]
            image_matrix[mapped_row][mapped_col] = tmp
    print(image_matrix)
    #flip
    for row in range(0, size//2 ):
        for col in range(0, size):
            print("row", row, "col", col)
            flipped_row = size - row -1
            print("flipped", flipped_row, col)
            temp = image_matrix[row][col]
            image_matrix[row][col] = image_matrix[flipped_row][col]
            image_matrix[flipped_row][col] = temp
    return image_matrix

def test():
    image = [[1,2], [3,4]]
    print(rotate_image(image))

test()