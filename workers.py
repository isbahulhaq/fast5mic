import asyncio

async def run_worker(worker_id: int, work_time: int = 5):
    """
    Simulates a single user / worker doing some async task
    """
    print(f"👤 Worker {worker_id} started")

    # simulate async work (API call, processing, etc.)
    await asyncio.sleep(work_time)

    print(f"✅ Worker {worker_id} finished")
    return worker_id
