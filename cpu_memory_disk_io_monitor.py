import asyncio
import time

import psutil


async def monitor_io(process_id, duration):
    process = psutil.Process(process_id)
    start_time = time.time()

    while time.time() - start_time < duration:
        io_counters = process.io_counters()
        print(f"读取字节数: {io_counters.read_bytes / 1024 / 1024} MB")
        print(f"写入字节数: {io_counters.write_bytes / 1024 / 1024} MB")
        await asyncio.sleep(1)


async def monitor_memory(process_id, duration):
    process = psutil.Process(process_id)
    start_time = time.time()

    while time.time() - start_time < duration:
        memory_info = process.memory_info()
        memory_percent = process.memory_percent()
        print(f"内存使用量: {memory_info.rss / (1024 * 1024):.2f} MB")
        print(f"内存使用率: {memory_percent:.2f}%")
        await asyncio.sleep(1)


async def monitor_cpu(process_id, duration):
    process = psutil.Process(process_id)
    start_time = time.time()

    while time.time() - start_time < duration:
        cpu_percent = process.cpu_percent(interval=1)
        print(f"CPU 使用率: {cpu_percent}%")
        await asyncio.sleep(1)


async def main():
    process_id = int(input("请输入进程ID："))
    duration = int(input("请输入监控时长（秒）："))

    tasks = [
        monitor_io(process_id, duration),
        monitor_memory(process_id, duration),
        monitor_cpu(process_id, duration)
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
