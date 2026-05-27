from pyscript import document
from js import navigator

# HTML elements
video = document.getElementById("video")
canvas = document.getElementById("canvas")
photo = document.getElementById("photo")

# Start camera
async def start_camera():

    stream = await navigator.mediaDevices.getUserMedia({
        "video": True
    })

    video.srcObject = stream

# Capture photo
def capture_photo(event):

    context = canvas.getContext("2d")

    # Set canvas size
    canvas.width = video.videoWidth
    canvas.height = video.videoHeight

    # Draw video frame on canvas
    context.drawImage(
        video,
        0,
        0,
        canvas.width,
        canvas.height
    )

    # Convert to image
    image_data = canvas.toDataURL("image/png")

    photo.src = image_data

# Connect button
document.getElementById(
    "captureBtn"
).onclick = capture_photo

# Run camera
import asyncio
asyncio.ensure_future(start_camera())