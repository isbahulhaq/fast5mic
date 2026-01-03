import asyncio
import nest_asyncio
from workers import run_worker

nest_asyncio.apply()

# 🔧 CONFIG (CHANGE ONLY HERE)
TOTAL_USERS = 5        # ← yahin se scale karo
WORK_TIME = 5          # seconds per user

async def main():
    print("🚀 Starting system")
    print(f"• Total users: {TOTAL_USERS}")
    print(f"• Work time per user: {WORK_TIME}s\n")

    tasks = [
        asyncio.create_task(run_worker(i + 1, WORK_TIME))
        for i in range(TOTAL_USERS)
    ]

    results = await asyncio.gather(*tasks)

    print("\n🎉 All users completed")
    print("Results:", results)

if __name__ == "__main__":
    asyncio.run(main())
