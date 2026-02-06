import json
from pathlib import Path

from src.utils.clean_text import clean_text
from src.parser.parse_basic import parse_basic

PROCESSED_DIR = Path("data/processed")
PARSED_DIR = Path("data/parsed")
PARSED_DIR.mkdir(parents=True, exist_ok=True)


def run():
    for txt_file in PROCESSED_DIR.glob("*.txt"):
        original_text = txt_file.read_text(encoding="utf-8", errors="ignore")
        cleaned_text = clean_text(original_text)

        profile = parse_basic(original_text)   # ✅ use original_text for name
        profile["resume_id"] = txt_file.stem

        out_path = PARSED_DIR / f"{txt_file.stem}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(profile, f, indent=2)

        print(f"Parsed: {txt_file.name}")


if __name__ == "__main__":
    run()
