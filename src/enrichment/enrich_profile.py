import re


# --------------------------------------------------
# NORMALIZE TEXT
# --------------------------------------------------
def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


# --------------------------------------------------
# ORGANIZATION CLEANING (STRICT + REALISTIC)
# --------------------------------------------------
def clean_organizations(orgs):
    """
    Keeps only real company / institution names.
    Removes ML terms, roles, skills, libraries, noise.
    """

    blacklist_keywords = [
    # roles
    "associate", "engineer", "scientist", "executive",

    # ML / DS terms
    "ml", "ds", "ml & ds", "machine learning", "deep learning",
    "data science", "artificial intelligence", "ai",

    # skills / libs
    "python", "sql", "numpy", "pandas",
    "xgboost", "sklearn", "scikit", "pytorch",
    "tensorflow", "keras", "scipy", "seaborn",

    # misc noise
    "eda", "project", "tool", "documentation",
    "responsibilities", "performed"
]


    valid = []

    for org in orgs:
        org = normalize(org)
        lower = org.lower()

        # very short strings are noise
        if len(org) < 5:
            continue

        # blacklist keywords
        if any(k in lower for k in blacklist_keywords):
            continue

        # must look like a company (capital letters)
        if not re.search(r"[A-Z]{2,}", org):
            continue

        # numbers usually mean noise
        if re.search(r"\d", org):
            continue

        valid.append(org)

    return sorted(set(valid))


# --------------------------------------------------
# EDUCATION EXTRACTION
# --------------------------------------------------
def extract_education(orgs):
    """
    Extracts educational institutions from organizations.
    """

    edu_keywords = [
        "university", "college", "institute",
        "school", "board", "pune"
    ]

    return sorted({
        org for org in orgs
        if any(k in org.lower() for k in edu_keywords)
    })


# --------------------------------------------------
# LOCATION EXTRACTION (FALLBACK USING RAW TEXT)
# --------------------------------------------------
def extract_locations(text: str):
    """
    Regex-based fallback for city extraction from raw resume text.
    """

    cities = {
        "pune": "Pune",
        "bengaluru": "Bangalore",
        "bangalore": "Bangalore",
        "mumbai": "Mumbai",
        "delhi": "Delhi",
        "hyderabad": "Hyderabad"
    }

    found = []
    text_lower = text.lower()

    for key, value in cities.items():
        if key in text_lower:
            found.append(value)

    return sorted(set(found))


# --------------------------------------------------
# DATE CLEANING
# --------------------------------------------------
def clean_dates(dates):
    clean = []

    for d in dates:
        d = normalize(d)

        if re.search(r"(19|20)\d{2}", d):
            clean.append(d)

    return sorted(set(clean))


# --------------------------------------------------
# MAIN ENRICH FUNCTION
# --------------------------------------------------
def enrich_profile(basic_profile: dict, entities: dict, raw_text: str = ""):
    """
    Combines basic parsing + NER entities + fallback logic
    into a clean enriched resume profile.
    """

    enriched = basic_profile.copy()

    # ---- ORGANIZATIONS
    orgs = clean_organizations(entities.get("ORG", []))
    enriched["organizations"] = orgs

    # ---- EDUCATION
    enriched["education"] = extract_education(orgs)

    # ---- LOCATIONS (fallback)
    enriched["locations"] = extract_locations(raw_text)

    # ---- DATES
    enriched["dates"] = clean_dates(entities.get("DATE", []))

    return enriched
