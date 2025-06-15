import re
from .rules import suspicious_keywords

def is_phishing(text):
    text_lower = text.lower()
    score = 0

    for word in suspicious_keywords:
        if word in text_lower:
            score += 1

    if re.search(r"http[s]?://|www\.|bit\.ly|tinyurl", text_lower):
        score += 2

    return score >= 2  # threshold
