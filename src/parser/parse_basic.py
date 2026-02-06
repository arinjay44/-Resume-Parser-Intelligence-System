import re

def parse_basic(text: str) -> dict:
    profile = {
        "name": None,
        "email": None,
        "phone": None,
        "skills": []
    }

    # keep non-empty lines
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    # ---------------- EMAIL ----------------
    email_match = re.search(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", text)
    if email_match:
        profile["email"] = email_match.group(0)

    # ---------------- PHONE ----------------
    # supports +91, spaces/dashes, 10 digits
    phone_match = re.search(r"(\+?\d{1,3}[\s\-]?)?(\d[\s\-]?){10,12}", text)
    if phone_match:
        # clean spaces/dashes
        raw = phone_match.group(0)
        profile["phone"] = re.sub(r"\s|\-", "", raw)

    # ---------------- NAME ----------------
    # 1) Try label patterns: "Name: XYZ", "Candidate Name - XYZ"
    name_label = re.search(
        r"(?im)^\s*(name|candidate\s*name)\s*[:\-]\s*([A-Za-z][A-Za-z.\s]{2,60})\s*$",
        text
    )
    if name_label:
        profile["name"] = name_label.group(2).strip()
    else:
        # 2) Fallback: pick best candidate from top N lines
        # Skip lines that look like headings or contain contact/role words
        stop_words = {
            "resume", "cv", "profile", "summary", "experience", "education", "skills",
            "projects", "certifications", "objective", "work", "linkedin", "github"
        }

        def looks_like_name(candidate: str) -> bool:
            c = candidate.strip()
            if not (5 <= len(c) <= 45):
                return False

            low = c.lower()

            # reject if contains email/phone-like stuff
            if "@" in c:
                return False
            if re.search(r"\d", c):  # names usually don’t have digits
                return False

            # reject headings
            for w in stop_words:
                if w in low:
                    return False

            # accept 2-4 words, mostly alphabetic
            parts = c.split()
            if not (2 <= len(parts) <= 4):
                return False

            # each part should start with a letter
            if not all(p[0].isalpha() for p in parts):
                return False

            # reject if too many short words
            if sum(1 for p in parts if len(p) <= 1) > 0:
                return False

            return True

        # check top 12 lines
        for line in lines[:12]:
            # remove punctuation except spaces and dots
            cleaned = re.sub(r"[^A-Za-z.\s]", " ", line)
            cleaned = re.sub(r"\s+", " ", cleaned).strip()

            # some resumes have "Arinjay Bhosale" on first line (good)
            # some have "Associate Data Scientist" (bad) - filtered by stop_words
            if looks_like_name(cleaned):
                profile["name"] = cleaned
                break

        # ---------------- SKILLS (clean) ----------------
    skill_keywords = {
        "python","sql","excel","power bi","tableau","pandas","numpy","scikit-learn","sklearn",
        "tensorflow","pytorch","nlp","machine learning","deep learning","statistics",
        "linux","windows","mongodb","flask","seaborn","matplotlib"
    }

    found = set()

    for line in lines:
        low = line.lower()

        # remove headings like "languages:", "operating systems:", etc.
        low = re.sub(r"^(languages|tools|technologies|tech stack|operating systems|database|packages)\s*:\s*", "", low)

        # split by comma / pipe / bullet separators
        parts = re.split(r"[,|/•\-]+", low)

        for p in parts:
            p = p.strip()

            # ignore long sentences / junk
            if len(p) > 30:
                continue
            if re.search(r"\d", p):
                continue
            if len(p) < 2:
                continue

            # normalize common variants
            if p == "sklearn":
                p = "scikit-learn"

            # keep only known skills
            if p in skill_keywords:
                found.add(p)

    profile["skills"] = sorted(found)

    # FINAL fallback: if still None, take first line if it looks like a name
    if profile["name"] is None and lines:
        first = re.sub(r"[^A-Za-z.\s]", " ", lines[0])
        first = re.sub(r"\s+", " ", first).strip()
        if 2 <= len(first.split()) <= 4 and not re.search(r"\d|@", first):
            profile["name"] = first

    return profile
