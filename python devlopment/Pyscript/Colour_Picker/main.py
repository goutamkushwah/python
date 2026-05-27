from pyscript import document

# Apply selected color
def apply_color(event):

    # Get color value
    color = document.getElementById("colorPicker").value

    # Change background
    document.body.style.background = color

    # Show HEX code
    document.getElementById(
        "colorCode"
    ).innerText = f"HEX: {color}"

# Connect button
document.getElementById(
    "applyBtn"
).onclick = apply_color