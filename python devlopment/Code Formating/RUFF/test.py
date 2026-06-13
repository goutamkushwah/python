# Before formating
# import os
# import sys

# x=10

# print(x)
"""

outputreformatted test.py


F401 [*] `sys` imported but unused
 --> test.py:2:8
  |
1 | import os
2 | import sys
  |        ^^^
3 |
4 | x=10
  |
"""

# After formating
import os
import sys

x = 10

print(x)
