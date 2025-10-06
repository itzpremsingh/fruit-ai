from json import load

from ai.levenshtein import levenshtein


def loadFruits(path: str) -> list[str]:
    with open(path, "r") as f:
        return load(f)


def getBestMatches(word: str, fruits: list[str]) -> dict[int, list[str]]:
    """Return fruits grouped by similarity distance."""
    topDistance: dict[int, list[str]] = {}

    for fruit in fruits:
        distance = levenshtein(word, fruit)
        topDistance.setdefault(distance, []).append(fruit)

    return topDistance
