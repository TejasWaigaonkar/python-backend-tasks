import asyncio
import time

def timer(func):
    async def wrapper():
        start = time.time()
        await func()
        end = time.time()
        print("Time taken:", round(end - start, 2), "seconds")
    return wrapper

async def task1():
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(3)
    print("Task 2 completed")

@timer
async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())