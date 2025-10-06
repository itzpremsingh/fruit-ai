from core.matcher import getBestMatches, loadFruits

labels = {0: "Exact match", 1: "Small typo", 2: "Close match", 3: "Similar word"}

if __name__ == "__main__":
    fruits = loadFruits("data/fruits.json")

    name = input("Enter a fruit name: ").lower()
    bestMatches = getBestMatches(name, fruits)

    for distance, label in labels.items():
        if distance in bestMatches:
            print(f"{label}: {', '.join(bestMatches[distance])}")
