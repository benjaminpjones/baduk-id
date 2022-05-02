from bisect import bisect

_N = 361

_factorials = [1]
for i in range(1, 362):
    _factorials.append(i * _factorials[i-1])
# _factorials = [1, 1, 2, 6, 24, ... , N!]

def factorial(n):
    if n >= len(_factorials):
        raise ValueError(f"Requested a factorial outside pre-computed range: {n}!")
    return _factorials[n]

# binomial coefficient
def C(k, n):
    return factorial(n) // (factorial(k) * factorial(n-k))

# The number of board positions with (number of stones) == i
_num_boards_eq = [
    C(i, _N) * 2**i for i in range(_N)
]
# The number of board positions with (number of stones) <= i
_num_boards_lte = [_num_boards_eq[0]]
for i in range(1, _N):
    _num_boards_lte.append(_num_boards_lte[i-1] + _num_boards_eq[i])

def sum_combos(k, n_start, n_end):
    ret = 0
    for i in range(n_start, n_end):
        ret += C(k, i)
    return ret

# given a list of intersections (int[]), return a unique identifier
# This mapping corresponds to the lexicographic ordering on k elements:
#       ID          INTERSECTIONS
#        0             [0, 1, 2]
#        1             [0, 1, 3]
#        2             [0, 1, 4]
#        .                ...
#   C(361, 3) - 1   [359, 360, 361]
def combo_id(intersections):
    if len(intersections) == 0:
        return 1
    if len(intersections) == 1:
        return intersections[0]
    ret = sum_combos(len(intersections) - 1, _N - intersections[0], _N)
    for i in range(1, len(intersections)):
        k = len(intersections) - i
        n_start = _N - intersections[i]
        n_end = _N - intersections[i - 1] - 1
        ret += sum_combos(k - 1, n_start, n_end)
    return ret

def find_pos(prev_pos, num_stones, id):
    pos = prev_pos + 1
    combo_sum = 0
    while combo_sum <= id:
        curr_combo = C(num_stones - 1, _N - pos - 1)
        if combo_sum + curr_combo > id:
            break
        pos += 1
        combo_sum += curr_combo

    new_id = id - combo_sum
    return pos, new_id

def decode_cid(num_stones, id):
    if num_stones == 0:
        return []
    pos, id = find_pos(-1, num_stones, id)
    ret = [pos]

    num_stones -= 1
    
    while num_stones:
        pos, id = find_pos(ret[-1], num_stones, id)
        ret.append(pos)
        num_stones -= 1
    return ret

# convert a list of ones and zeros to a number
def bin_to_int(lst):
    ret = 0
    for el in lst:
        ret <<= 1
        ret += el
    return ret

# board: a 1-D array with N elements.  Each element can take on 3 values:
#     - 0: empty
#     - 1: black
#     - 2: white
def encode(board):
    num_stones = sum(1 for x in board if x != 0)
    if num_stones == 0:
        return 0
    c_id = combo_id([idx for idx, val in enumerate(board) if val != 0])
    bw_id = bin_to_int([val - 1 for val in board if val != 0])
    return _num_boards_lte[num_stones - 1] + c_id * 2**num_stones + bw_id

def decode(id):
    num_stones = bisect(_num_boards_lte, id)
    if num_stones == 0:
        return [0] * _N
    id -= _num_boards_lte[num_stones - 1]
    bw_id = id % 2**num_stones
    c_id = id // 2**num_stones
    intersections = decode_cid(num_stones, c_id)
    ret = [0] * _N
    for i in range(num_stones):
        if (1 << (num_stones - i - 1)) & bw_id:
            ret[intersections[i]] = 2
        else:
            ret[intersections[i]] = 1
    return ret
