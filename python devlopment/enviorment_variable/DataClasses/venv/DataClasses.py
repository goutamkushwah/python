from dataclasses import dataclass, field

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
item1 = InventoryItem('Widget', 3.0, 10)
print(item1)
print(f'Total cost of {item1.name}: {item1.total_cost()}')

@dataclass
class C:
    mylist: list[int] = field(default_factory=list)

c = C()
c.mylist += [1, 2, 3]
print(c.mylist)

@dataclass
class C:
    x: int
    y: int = field(repr=False)
    z: int = field(repr=False, default=10)
    t: int = 20
c = C(1, 2)
print(c)
@dataclass
class C:
    a: int       # 'a' has no default value
    b: int = 0   # assign a default value for 'b'

c1 = C(1)      # 'b' will take the default value of 0
print(c1)