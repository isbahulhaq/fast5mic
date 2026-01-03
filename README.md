# Async User Worker Project

This repository demonstrates a clean, scalable async architecture
for running multiple users/workers in parallel.

## Structure

- `setup.sh` – environment setup (run once)
- `requirements.txt` – dependencies
- `workers.py` – individual user/task logic
- `main.py` – orchestration & scaling
- `README.md` – documentation

## How to Run

```bash
bash setup.sh
python main.py
