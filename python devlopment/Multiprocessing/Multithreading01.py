import time

def download_file(url, filename):
    """Simulate downloading a file"""
    print(f"Starting download: {filename}")
    time.sleep(2)  # Simulate download time
    print(f"Completed: {filename}")
    return filename

def main():
    """Download files one by one (sequential)"""
    files = [
        ("https://www.youtube.com/watch?v=eRMrHZdUuFg&list=RDh4SPoOu7wL8&index=10", "video.mp4"),
        ("https://roadmap.sh/python", "document.pdf"),
        ("https://www.jiosaavn.com/song/phir-le-aya-dil/XVEsZB1JRQE", "music.mp3")
    ]

    print("=== Sequential Downloads ===")
    start_time = time.time()

    for url, filename in files:
        download_file(url, filename)

    total_time = time.time() - start_time
    print(f"Total time: {total_time:.1f} seconds")

if __name__ == "__main__":
    main()