import re


def parse_basic(text: str) -> dict:
    """
    Basic resume parsing (Day 2)
    Extracts name, email, phone (very simple heuristics)
    """

    profile = {
        "name": None,
        "email": None,
        "phone": None,
        "summary": None
    }

    # EMAIL
    email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    if email_match:
        profile["email"] = email_match.group()

    # PHONE (robust Indian + international)
    phone_match = re.search(
    r"(\+?\d{1,3}[\s-]?)?\(?\d{3,5}\)?[\s-]?\d{3,5}[\s-]?\d{4}",
    text
    )

    if phone_match:
        profile["phone"] = phone_match.group()

    # NAME (very naive — first non-empty line)
    for line in text.splitlines():
        line = line.strip()
        if 3 < len(line) < 50 and line.replace(" ", "").isalpha():
            profile["name"] = line
            break

    # SUMMARY (first 3 non-empty lines)
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    profile["summary"] = " ".join(lines[:3])

    return profile
