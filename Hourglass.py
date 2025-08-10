def max_hourglass_sum(arr: list[list[int]]) -> int:
    """
    Calculates the maximum hourglass sum in a 2D array.
    An hourglass is defined as:
      a b c
        d
      e f g
    The array must be at least 3x3.
    """
    if len(arr) < 3 or len(arr[0]) < 3:
        raise ValueError("Minimum 3 rows and 3 columns required")

    rowcount = len(arr) - 2
    colcount = len(arr[0]) - 2
    sumhourg = []

    for i in range(rowcount):
        for j in range(colcount):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            sumhourg.append(top + middle + bottom)

    return max(sumhourg)