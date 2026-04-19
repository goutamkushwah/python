class NegativeValueError(Exception):
    """Raised when a negative value is not allowed"""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative value not allowed: {value}")

def process_value(x):
    if x < 0:
        raise NegativeValueError(x)
    return x * 2

# Test
try:
    print(process_value(-5))
except NegativeValueError as e:
    print(e)
