import logging
import time
from pathlib import Path


class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        logging.info("Program was started")
        # сделала скорее для себя, для понимания работы

    def __exit__(self, exc_type, exc_value, traceback):
        # logger.info(...)
        end_time = time.time() - self.start_time
        # print(f"End time: {end_time}")
        logging.info(f"Program was completed, runtime - {end_time}")


# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

with TimerContext():
    time.sleep(2)

# test with another code
with TimerContext() as program:
    ROOT_DIR = Path(__file__).parent.parent

    file = open(ROOT_DIR / "rockyou.txt")
    # text: str = file.readline()
    counter = 0

    while True:
        try:
            word = file.readline()
            counter += 1
        except Exception:
            break
    file.close()
    print(counter)
