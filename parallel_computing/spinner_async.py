import itertools
import asyncio
from multiprocessing import Process, Event, synchronize
import time

def spin(msg: str, done: synchronize.Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
            
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def slow():
    time.sleep(3)
    return 42

async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'spinning object{spinner}')
    result = await slow()
    spinner.cancel()
    return result

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()