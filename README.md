# BadukID
Convert board state to a unique id.  Lower ids are assigned to boards with fewer stones.

Usage:

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
# The value of flying_knife_board will be equivalent to FLYING_KNIVE
flying_knife_board = decode(flying_knife_id)
```
