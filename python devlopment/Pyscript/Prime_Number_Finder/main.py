from pyscript import document

# Check prime number
def check_prime(event):

    num = int(
        document.getElementById(
            "numberInput"
        ).value or 0
    )

    result = document.getElementById("result")

    # Numbers less than 2 are not prime
    if num < 2:
        result.innerText = f"{num} is NOT a Prime Number"
        return

    # Assume number is prime
    is_prime = True

    # Check divisibility
    for i in range(2, num):

        if num % i == 0:
            is_prime = False
            break

    # Show result
    if is_prime:
        result.innerText = f"{num} is a Prime Number ✅"
    else:
        result.innerText = f"{num} is NOT a Prime Number ❌"

# Connect button
document.getElementById(
    "checkBtn"
).onclick = check_prime