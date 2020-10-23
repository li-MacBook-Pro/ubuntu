import asyncio
import time
# https://docs.python.org/zh-cn/3.7/library/asyncio.html?highlight=asyncio#module-asyncio
async def main0():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
# asyncio.run(main0())

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main1():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

# asyncio.run(main1())

# ~~~~~~~~~~~并发~~~~~~~~
async def main2():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")
asyncio.run(main2())
