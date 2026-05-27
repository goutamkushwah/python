from pyscript import document
from js import console

# result element
result = document.getElementById("result")

# functions
def get_values():
    num1 = float(document.getElementById("num1").value or 0)
    num2 = float(document.getElementById("num2").value or 0)

    return num1, num2

def add(event):
    a, b = get_values()
    result.innerText = f"Result: {a + b}"

def sub(event):
    a, b = get_values()
    result.innerText = f"Result: {a - b}"

def mul(event):
    a, b = get_values()
    result.innerText = f"Result: {a * b}"

def div(event):
    a, b = get_values()

    if b == 0:
        result.innerText = "Cannot divide by zero"
    else:
        result.innerText = f"Result: {a / b}"

# connect buttons AFTER page loads
document.getElementById("addBtn").onclick = add
document.getElementById("subBtn").onclick = sub
document.getElementById("mulBtn").onclick = mul
document.getElementById("divBtn").onclick = div

console.log("Calculator Loaded")