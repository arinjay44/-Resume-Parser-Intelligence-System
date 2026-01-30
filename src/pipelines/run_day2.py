import json
from pathlib import Path

from clean_text import clean_text
from src.parser.parse_basic import (
    extract_email,
    extract_phone,
    extract_name,
    extract_skills
)

PROCESSED_DIR = Path("data/processed")
PARSED_DIR = Path("data/parsed")
PARSED_DIR.mkdir(parents=True, exist_ok=True)

def run():
    for txt_file in PROCESSED_DIR.glob("*.txt"):
        original_text = txt_file.read_text(encoding="utf-8")
        cleaned_text = clean_text(original_text)

        profile = {
            "resume_id": txt_file.stem,
            "name": extract_name(original_text),
            "email": extract_email(cleaned_text),
            "phone": extract_phone(cleaned_text),
            "skills": extract_skills(cleaned_text)
        }

        out_path = PARSED_DIR / f"{txt_file.stem}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(profile, f, indent=2)

        print(f"Parsed: {txt_file.name}")

if __name__ == "__main__":
    run()
