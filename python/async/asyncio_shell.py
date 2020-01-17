# coding:utf-8
import time 
import asyncio
from asyncio.subprocess import PIPE, STDOUT 

sem = asyncio.Semaphore(2)


async def run_cmd(n):
    cmd = "sleep 5 && echo `date`"
    start = time.time()
    print (f"[INFO] Starting script...{n}.. {start}")
    process = await asyncio.create_subprocess_shell(cmd, stdin = PIPE, stdout = PIPE, stderr = STDOUT)
    await process.wait()
    stdout, _ = await process.communicate()
    print(f"[INFO] Script is complete. {n}...{int(time.time() - start)}....{stdout.decode().strip()}")

async def run_cmd2(n):
    cmd = "python cpu_high.py"
    async with sem:
    # if True:
        start = time.time()
        print (f"[INFO] Starting script...{n}.. {start}")
        process = await asyncio.create_subprocess_shell(cmd, stdin = PIPE, stdout = PIPE, stderr = STDOUT)
        await process.wait()
        stdout, _ = await process.communicate()
        print(f"[INFO] Script is complete. {n}...{int(time.time() - start)}....{stdout.decode().strip()}")

async def main():
    print(time.time())
    await asyncio.sleep(3)
    print(time.time())

if __name__ == "__main__":
    loop = asyncio.get_event_loop() 
    tasks = [loop.create_task(main())]
    for i in range(5):
        tasks.append(loop.create_task(run_cmd(i)))
    for i in range(5, 10):
        tasks.append(loop.create_task(run_cmd2(i)))
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

