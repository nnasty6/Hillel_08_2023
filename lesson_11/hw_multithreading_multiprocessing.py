import os
import threading
import time
from multiprocessing import Process
from threading import Thread

import requests

URL_IM = (
    "https://cdn.pixabay.com/photo/2023/09/24/20/01/mushroom-8273752_1280.jpg"
)


# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    print(f"\n📄 Processing data from {path} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        with open("image.jpg", "wb") as f:
            f.write(response.content)
        print(
            f"\n🌠 Downloading image from {image_url} "
            f"in thread {threading.current_thread().name}"
        )
    except Exception as e:
        print(f"Error occurred: {e}")


def thread_func(func, filename):
    threads = [
        Thread(
            target=func,
            args=(filename,),
        )
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def process_func(func, filename):
    tasks = [
        Process(
            target=func,
            args=[filename],
        )
    ]

    for task in tasks:
        task.start()

    for task in tasks:
        task.join()


if __name__ == "__main__":
    encryption_process_time = time.perf_counter()
    process_func(encrypt_file, "rockyou.txt")
    encryption_process_counter = time.perf_counter() - encryption_process_time

    print(
        "⏱️ Time taken for encryption task "
        f"process: {encryption_process_counter}"
    )

    download_tread_time = time.perf_counter()
    thread_func(download_image, URL_IM)
    download_tread_counter = time.perf_counter() - download_tread_time

    print(f"⏱️ Time taken for download task tread: {download_tread_counter} ")

    print(
        f"\nProcess = {encryption_process_counter}\n"
        f"Tread = {download_tread_counter}\n"
        f"⏰ Total time = {encryption_process_counter+download_tread_counter}\n"
    )
