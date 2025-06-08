import itertools
import time
from threading import Thread, Event

def spin(msg: str, done: Event) -> None:  # <1>
    for char in itertools.cycle(r'\|/-'):  # <2>
        status = f'\r{char} {msg}'  # <3>
        print(status, end='', flush=True)
        if done.wait(.1):  # <4>
            break  # <5>
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')  # <6>

def slow() -> int:
    time.sleep(3)  # <7>
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('thinking!', done))

    print(f'spinner object: {spinner}')

    spinner.start()
    result = slow()
    done = set()
    spinner.join()

    return result

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')

if __name__ == 'main':
    main()