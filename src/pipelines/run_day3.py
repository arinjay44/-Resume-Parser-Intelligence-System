from src.extraction.extract_text import extract_text
from src.parser.parse_basic import parse_basic
from src.ner.ner_extractor import extract_entities
from src.enrichment.enrich_profile import enrich_profile
from pathlib import Path

def main():
    resume_path = "data/raw/Arinjay Bhosale Final_Resume.pdf"

    # DEBUG: check file exists
    print("FILE EXISTS:", Path(resume_path).exists())

    raw_text = extract_text(resume_path)
    print("RAW TEXT LENGTH:", len(raw_text))
    print("RAW TEXT CONTAINS PUNE:", "pune" in raw_text.lower())

    basic_profile = parse_basic(raw_text)
    entities = extract_entities(raw_text)

    enriched_profile = enrich_profile(basic_profile, entities, raw_text)

    print("\nENRICHED PROFILE\n")
    print(enriched_profile)


if __name__ == "__main__":
    main()
