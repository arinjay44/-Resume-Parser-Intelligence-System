import pdfplumber
from docx import Document
from pathlib import Path


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
    """
    Unified resume text extractor
    Supports: PDF, DOCX
    """
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
