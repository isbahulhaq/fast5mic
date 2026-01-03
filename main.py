import argparse
import asyncio
import nest_asyncio
import yaml
from workers import run_worker

nest_asyncio.apply()

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--users", type=int, help="Number of users")
    parser.add_argument("--work-time", type=int, help="Work time per user (seconds)")
    args = parser.parse_args()

    cfg = load_config()

    total_users = args.users if args.users is not None else cfg.get("users", 5)
    work_time = args.work_time if args.work_time is not None else cfg.get("work_time", 5)

    print("🚀 Fast5Mic")
    print(f"• Users: {total_users}")
    print(f"• Work time: {work_time}s\n")

    tasks = [
        asyncio.create_task(run_worker(i + 1, work_time))
        for i in range(total_users)
    ]

    results = await asyncio.gather(*tasks)
    print("\n🎉 All users completed:", results)

if __name__ == "__main__":
    asyncio.run(main())
