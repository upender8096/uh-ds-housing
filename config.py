## === config.py ===
# 
from pathlib import Path

# --- Path Configuration ---
PROJECT_DIR = Path(r"C:\Users\BALA\OneDrive - University of Hertfordshire\Desktop\Upendra project\uh-ds-housing")
DATA_DIR = Path(r"C:\DataProjects\uh-ds-housing-data\data")

RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

# Ensure folders exist
for d in [RAW_DIR, INTERIM_DIR, PROCESSED_DIR]:
    d.mkdir(parents=True, exist_ok=True)
