import time
from datetime import datetime


class timer(object):
    def __enter__(self):
        self.t = time.time()
        print(f'>> Start {datetime.now().strftime("%H:%M:%S.%f")}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'>> Stop {datetime.now().strftime("%H:%M:%S.%f")}')
        print(f'>> Spend {time.time() - self.t}')


with timer():
    with open('lorem.txt', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
