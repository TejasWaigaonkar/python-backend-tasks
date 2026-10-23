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

# async def brew(name):
#     print(f"Brewing {name}")
#     await asyncio.sleep(2)
#     print(f"{name} is ready")

# async def main():
#     await asyncio.gather(
#         brew("Masala chai"),
#         brew("elaichi chai"),
#         brew("ginger chai")
#     )

# asyncio.run(main())
#--------------------------------------
