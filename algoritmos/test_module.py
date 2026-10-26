"""Scratch module for testing small algorithm ideas."""

def are_anagrams(word1: str, word2: str) -> bool:
    """Check if two words are anagrams (case-insensitive)."""
    w1 = word1.replace(" ", "").lower()
    w2 = word2.replace(" ", "").lower()
    return sorted(w1) == sorted(w2)


print(are_anagrams("apas", "apa"))
