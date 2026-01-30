import re
import logging

logger = logging.getLogger(__name__)

class ResumePreprocessor:

    def __init__(self):
        logger.info("Preprocessor Initialized")

    def clean_text(self, text: str):
        try:
            logger.info("Cleaning text...")

            text = text.replace("\n", " ")           # remove line breaks
            text = re.sub(r'\s+', ' ', text)         # handle extra spaces
            text = text.strip()

            return text

        except Exception as e:
            logger.error(f"Preprocessing failed: {e}")
            raise