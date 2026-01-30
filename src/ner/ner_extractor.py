import spacy
from collections import defaultdict

nlp = spacy.load("en_core_web_sm")

ALLOWED_ENTITIES = {"PERSON", "ORG", "DATE", "GPE", "LOC"}

def extract_entities(text: str):
    doc = nlp(text)

    entities = defaultdict(set)

    for ent in doc.ents:
        if ent.label_ in ALLOWED_ENTITIES:
            entities[ent.label_].add(ent.text.strip())

    # convert sets to sorted lists
    return {k: sorted(v) for k, v in entities.items()}
