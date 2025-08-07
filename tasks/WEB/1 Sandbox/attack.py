# attack.py
import asyncio
import aiohttp
import time

URL = "http://127.0.0.1:5000/ping"
CONCURRENT_REQUESTS = 1000  # зміни на більше/менше

async def spam(session):
    try:
        async with session.get(URL) as resp:
            await resp.text()
    except Exception as e:
        pass  # Сервер може дропати запити — норм

async def attack():
    async with aiohttp.ClientSession() as session:
        tasks = [spam(session) for _ in range(CONCURRENT_REQUESTS)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(attack())
    print("Done in", time.time() - start, "seconds")
