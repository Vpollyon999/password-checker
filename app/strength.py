MIN_LENGTH = 8
LONG_LENGTH = 12


def score_password(password):
    """Return a score from 0 to 5 based on length and character variety."""
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    score = 0
    if len(password) >= MIN_LENGTH:
        score += 1
    if len(password) >= LONG_LENGTH:
        score += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1
    return score


def strength_label(password):
    """Return 'weak', 'medium' or 'strong'."""
    score = score_password(password)
    if score <= 2:
        return "weak"
    if score == 3:
        return "medium"
    return "strong"
