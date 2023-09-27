import multiprocessing
import os
import threading
import time

import requests


# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    print(f"Processing image from {image_url} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(
        f"Downloading image from {image_url}"
        f" in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    image_url = "https://example.com/image.jpg"

    start_time = time.perf_counter()

    download_thread = threading.Thread(
        target=download_image, args=(image_url,)
    )
    download_thread.start()
    download_thread.join()

    mid_time = time.perf_counter()

    encrypt_process = multiprocessing.Process(
        target=encrypt_file, args=("image.jpg",)
    )
    encrypt_process.start()
    encrypt_process.join()

    end_time = time.perf_counter()

    print(f"Download took {mid_time - start_time} seconds")
    print(f"Encryption took {end_time - mid_time} seconds")
