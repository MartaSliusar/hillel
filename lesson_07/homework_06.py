import logging
import time


class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        execution_time = time.time() - self.start_time
        logging.info(f"execution_time: {execution_time}")


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

with TimerContext():
    time.sleep(2)
