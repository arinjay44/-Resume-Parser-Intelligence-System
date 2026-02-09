import json
from pathlib import Path

from src.extraction.extract_text import extract_text
from src.parser.parse_basic import parse_basic
from src.ner.ner_extractor import extract_entities
from src.enrichment.enrich_profile import enrich_profile


RAW_DIR = Path("data/raw")
ENRICHED_DIR = Path("data/enriched")
ENRICHED_DIR.mkdir(parents=True, exist_ok=True)


def run():
    # Process every pdf/docx in data/raw
    resume_files = list(RAW_DIR.glob("*.pdf")) + list(RAW_DIR.glob("*.docx"))

    if not resume_files:
        print("No resumes found in data/raw (pdf/docx).")
        return

    for resume_path in resume_files:
        raw_text = extract_text(str(resume_path))
        basic_profile = parse_basic(raw_text)
        entities = extract_entities(raw_text)
        enriched_profile = enrich_profile(basic_profile, entities, raw_text)

        out_path = ENRICHED_DIR / f"{resume_path.stem}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(enriched_profile, f, indent=2, ensure_ascii=False)

        print(f"Enriched: {out_path.name}")


if __name__ == "__main__":
    run()
