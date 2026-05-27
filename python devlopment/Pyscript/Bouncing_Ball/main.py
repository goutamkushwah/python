from pyscript import document
from js import window
from pyodide.ffi import create_proxy
import math

# Canvas
canvas = document.getElementById("canvas")

ctx = canvas.getContext("2d")

# Ball position
x = 100
y = 100

# Ball speed
dx = 4
dy = 3

# Ball radius
radius = 25

# Animation function
def animate():

    global x, y, dx, dy

    # Clear canvas
    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    )

    # Draw ball
    ctx.beginPath()

    ctx.arc(
        x,
        y,
        radius,
        0,
        math.pi * 2
    )

    ctx.fillStyle = "blue"

    ctx.fill()

    ctx.closePath()

    # Move ball
    x += dx
    y += dy

    # Bounce left/right
    if x + radius >= canvas.width or x - radius <= 0:
        dx = -dx

    # Bounce top/bottom
    if y + radius >= canvas.height or y - radius <= 0:
        dy = -dy

# IMPORTANT:
# Create stable JS proxy
animate_proxy = create_proxy(
    lambda: animate()
)

# Start animation
window.setInterval(
    animate_proxy,
    16
)