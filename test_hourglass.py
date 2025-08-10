from Hourglass import max_hourglass_sum

def test_basic_hourglass():
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    assert max_hourglass_sum(arr) == 19

def test_hourglass_sum_basic():
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
    expected = 19
    result = max_hourglass_sum(arr)
    assert result == expected

def test_negative_values():
    arr = [
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    assert max_hourglass_sum(arr) == 28

def test_all_zeros():
    arr = [[0]*6 for _ in range(6)]
    assert max_hourglass_sum(arr) == 0

def test_too_small():
    arr = [[1, 2], [3, 4]]
    try:
        max_hourglass_sum(arr)
        assert False, "Expected ValueError"
    except ValueError:
        pass