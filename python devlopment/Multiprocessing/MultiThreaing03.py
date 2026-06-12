# basic_threading.py

import threading
import time

def download_file(url, filename):
    """Download a single file"""
    thread_name = threading.current_thread().name

    print(f"[{thread_name}] Starting: {filename}")
    time.sleep(2)  # Simulate download time
    print(f"[{thread_name}] Completed: {filename}")

def threaded_downloads():
    """Download files using multiple threads"""

    files = [
        ("https://example.com/video.mp4", "video.mp4"),
        ("https://example.com/document.pdf", "document.pdf"),
        ("https://example.com/music.mp3", "music.mp3")
    ]

    print("=== Multi-Threaded Downloads ===")
    start_time = time.time()

    threads = []

    # Create threads
    for url, filename in files:
        thread = threading.Thread(
            target=download_file,
            args=(url, filename),
            name=f"Downloader-{filename.split('.')[0]}"
        )
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    total_time = time.time() - start_time
    print(f"Threaded time: {total_time:.1f} seconds")

if __name__ == "__main__":
    threaded_downloads()