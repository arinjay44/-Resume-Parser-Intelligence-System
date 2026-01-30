import os


# -------- PROJECT ROOT --------
PROJECT_ROOT = os.getcwd()

# -------- DATA PATHS --------
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")


# -------- SUPPORTED FILES --------
SUPPORTED_EXTENSIONS = (".pdf", ".docx")


# -------- ENSURE DIRECTORIES EXIST --------
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
