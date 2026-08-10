# carga.py
import asyncio, datetime, platform, time, httpx
print(datetime.datetime.now().isoformat(), platform.node(), platform.platform())

async def main(url, n=20):
    t0 = time.perf_counter()
    async with httpx.AsyncClient(timeout=30) as c:
        r = await asyncio.gather(*[c.get(url) for _ in range(n)])
        print(url, "completadas:", sum(x.status_code == 200 for x in r),
        "en", round(time.perf_counter() - t0, 2), "s")

asyncio.run(main("http://127.0.0.1:8001/lento"))
asyncio.run(main("http://127.0.0.1:8002/lento"))