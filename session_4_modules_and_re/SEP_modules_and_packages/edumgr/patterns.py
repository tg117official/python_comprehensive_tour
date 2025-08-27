# Regex patterns & helpers
import re

# Simple, practical patterns (kept beginner-friendly)
EMAIL_RE = re.compile(r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$", re.IGNORECASE)
ROLL_RE  = re.compile(r"^[0-9]{1,8}$")  # e.g., 1023  (tweak as needed)
SUBJECT_SPLIT_RE = re.compile(r"\s*,\s*")
MARK_RE = re.compile(r"^\s*(\d{1,3})(?:\s*/\s*(\d{1,3}))?\s*$")  # "90" or "90/100"

def is_valid_email(s: str) -> bool:
    return EMAIL_RE.match(s or "") is not None

def is_valid_roll(s: str) -> bool:
    return ROLL_RE.match(s or "") is not None

def split_subjects(s: str):
    # Returns list of trimmed subjects (no empties)
    if not s:
        return []
    return [x for x in SUBJECT_SPLIT_RE.split(s.strip()) if x]

def parse_mark(s: str):
    """
    Returns (score, out_of) parsed from strings like:
      "90" -> (90, None)
      "90/100" -> (90, 100)
    Raises ValueError if not matching.
    """
    m = MARK_RE.match(s or "")
    if not m:
        raise ValueError("Invalid mark format. Use '90' or '90/100'.")
    score = int(m.group(1))
    out_of = int(m.group(2)) if m.group(2) else None
    return score, out_of
