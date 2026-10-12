"""Small utility module used to demonstrate CI quality gates."""
import os

def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def divide(a: float, b: float) -> float:
    """Return a divided by b. Raises ValueError when b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_palindrome(text: str) -> bool:
    """Case-insensitive palindrome check that ignores non-alphanumerics."""
    cleaned = [c.lower() for c in text if c.isalnum()]
    return cleaned == cleaned[::-1]


def grade(score: int) -> str:
    """Convert a numeric score (0-100) to a letter grade."""
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
