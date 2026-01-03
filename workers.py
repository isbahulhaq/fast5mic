import asyncio

async def run_worker(worker_id: int, work_time: int = 5):
    print(f"👤 Worker {worker_id} started")
    await asyncio.sleep(work_time)
    print(f"✅ Worker {worker_id} finished")
    return worker_id
