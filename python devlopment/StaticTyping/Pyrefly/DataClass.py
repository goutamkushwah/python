# Example: Dataclasses

from dataclasses import dataclass

@dataclass
class Point:
  x: float
  y: float

Point(x=0.0, y=0.0)    # OK
Point(x=0.0, y="oops") # ERROR!
