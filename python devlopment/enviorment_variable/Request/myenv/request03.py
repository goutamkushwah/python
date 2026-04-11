import requests
from PIL import Image
from io import BytesIO

# 1. Fetch an image from a URL
url = 'https://raw.githubusercontent.com/python-pillow/Pillow/master/docs/conf.py' 
# Let's use a real image placeholder for this example
url = 'https://picsum.photos/400/300'

r = requests.get(url)

# 2. Check if the request was successful
if r.status_code == 200:
    # 3. Open the byte stream as an image
    i = Image.open(BytesIO(r.content))
    
    # 4. Display metadata
    print(f"Format: {i.format}")  # e.g., JPEG, PNG
    print(f"Size:   {i.size}")    # (width, height)
    print(f"Mode:   {i.mode}")    # e.g., RGB, RGBA, L (grayscale)
    
    # 5. Optional: Show the image or save it
    # i.show()
    # i.save('downloaded_image.png')
else:
    print(f"Failed to retrieve image. Status code: {r.status_code}")