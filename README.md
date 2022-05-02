# BadukID
Convert board state to a unique id.  This ID is an integer in the range \[0, 3^361).  Lower ids are assigned to boards with fewer stones.

## Installation

```
python3 -m pip install baduk-id
```

## Usage

```
from baduk_id.baduk_id import encode, decode

# board state should be a 1-D array with 361 elements
# 0=empty 1=black, 2=white
FLYING_KNIFE = (
    [0] * 19
    + [0] * 12 + [1, 2, 0, 0, 0, 0, 0]
    + [0] * 12 + [0, 1, 2, 2, 2, 0, 0]
    + [0] * 12 + [0, 1, 2, 1, 1, 0, 0]
    + [0] * 12 + [0, 0, 1, 2, 0, 0, 0]
    + [0] * 19 * 14)

flying_knife_id = encode(FLYING_KNIFE)
# The value of board_state will be equivalent to FLYING_KNIVE
board_state = decode(flying_knife_id)
```
