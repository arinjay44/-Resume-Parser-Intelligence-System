import re
import pdfplumber
from docx import Document
from pathlib import Path


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def extract_pdf(path: Path) -> str:
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_docx(path: Path) -> str:
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)


def extract_text(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Resume not found: {file_path}")

    suffix = path.suffix.lower()

    if suffix == ".pdf":
        return extract_pdf(path)
    elif suffix == ".docx":
        return extract_docx(path)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")


def safe_stem(p: Path) -> str:
    # removes weird chars from filename
    s = re.sub(r"[^a-zA-Z0-9_-]+", "_", p.stem)
    return s.strip("_") or "resume"


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    files = list(RAW_DIR.glob("*.pdf")) + list(RAW_DIR.glob("*.docx"))

    if not files:
        print("No PDF/DOCX files found in data/raw")
        return

    for f in files:
        try:
            text = extract_text(str(f))
            out_file = PROCESSED_DIR / f"{safe_stem(f)}.txt"
            out_file.write_text(text, encoding="utf-8", errors="ignore")
            print(f"Saved: {out_file}")
        except Exception as e:
            print(f"Failed: {f.name} -> {e}")


if __name__ == "__main__":
    main()
