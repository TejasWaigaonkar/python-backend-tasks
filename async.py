import asyncio
import time

# async def brew_chai():
#     print("Brewing chai....")
#     await asyncio.sleep(2)
#     print("Chai is ready")

# asyncio.run(brew_chai())
#---------------------------------------------

async def brew(name):
    print(f"Brewing {name}")
    time.sleep(3)
    print(f"{name} is ready")

async def main():
    await asyncio.gather(
        brew("Masala chai"),
        brew("elaichi chai"),
        brew("ginger chai")
    )

asyncio.run(main())
#--------------------------------------------

async def brew(name):
    print(f"Brewing {name}")
    await asyncio.sleep(2)
    print(f"{name} is ready")

async def main():
    await asyncio.gather(
        brew("Masala chai"),
        brew("elaichi chai"),
        brew("ginger chai")
    )

asyncio.run(main())
#--------------------------------------

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
