def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    my_arr = [[1]]

    for i in range(1, n):  # Start from the second row
        row = [1]  # First element of each row is always 1
        for j in range(1, i):  # Generate the intermediate elements
            row.append(my_arr[i-1][j-1] + my_arr[i-1][j])
        row.append(1)  # Last element of each row is always 1
        my_arr.append(row)

    return my_arr
