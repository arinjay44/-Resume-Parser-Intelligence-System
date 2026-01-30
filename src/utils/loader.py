import os
import docx
import pdfplumber
from src.utils.logger import get_logger
from src.utils.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, SUPPORTED_EXTENSIONS


logger = get_logger("RESUME_LOADER")


class ResumeLoader:

    def __init__(self):
        logger.info("Resume Loader Initialized")

    def list_resumes(self):
        resumes = [
            file for file in os.listdir(RAW_DATA_DIR)
            if file.lower().endswith(SUPPORTED_EXTENSIONS)
        ]

        logger.info(f"Found {len(resumes)} resumes")
        return resumes

    def read_docx(self, path):
        doc = docx.Document(path)
        return "\n".join([p.text for p in doc.paragraphs])

    def read_pdf(self, path):
        text = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    def extract_text(self, filename):
        full_path = os.path.join(RAW_DATA_DIR, filename)

        if filename.lower().endswith(".pdf"):
            return self.read_pdf(full_path)

        elif filename.lower().endswith(".docx"):
            return self.read_docx(full_path)

        else:
            logger.warning(f"Unsupported file skipped: {filename}")
            return ""

    def process_and_save(self):
        resumes = self.list_resumes()

        for resume in resumes:
            try:
                text = self.extract_text(resume)

                if not text.strip():
                    logger.warning(f"No text extracted from {resume}")
                    continue

                output_file = resume.replace(".pdf", ".txt").replace(".docx", ".txt")
                output_path = os.path.join(PROCESSED_DATA_DIR, output_file)

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text)

                logger.info(f"Processed and saved: {resume}")

            except Exception as e:
                logger.error(f"Failed processing {resume} | Error: {str(e)}")


if __name__ == "__main__":
    loader = ResumeLoader()
    loader.process_and_save()
