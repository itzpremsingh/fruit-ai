# 🍎 Fruit AI

A small Python project that finds similar fruit names using the **Levenshtein distance** algorithm — detects typos, spelling mistakes, and close matches.
[Live demo]()

## 🚀 Live Demo
You can try the Fruit AI project online here:  
[🔗 Fruit AI Live Demo](https://itzpremsingh.github.io/html/fruit-ai/index.html)

---

## 📂 Project Structure

```
fruit-ai/
│
├── data/
│   └── fruits.json          # list of fruits
│
├── ai/
│   └── levenshtein.py       # Levenshtein algorithm
│
├── core/
│   └── matcher.py           # match and group similar fruits
│
└── main.py                  # user interface
```

---

## ⚙️ Requirements

- Python 3.9+
- No third-party packages needed

---

## 📥 Clone the Project

```bash
git clone https://github.com/itzpremsingh/fruit-ai.git
cd fruit-ai
```

---

## 🚀 Run the Project

### Option 1 — Recommended (proper package run)

```bash
python -m fruit-ai.main
```

### Option 2 — Direct path (works from anywhere)

```bash
python /path/to/fruit-ai/main.py
```

Replace `/path/to/fruit-ai/` with the actual path on your system.

---

## 🧠 How It Works

- Uses **Levenshtein distance** to compare the input word with each fruit name.
- Groups results by distance value:

  | Distance | Meaning      |
  | -------- | ------------ |
  | 0        | Exact match  |
  | 1        | Small typo   |
  | 2        | Close match  |
  | 3        | Similar word |

---

## 🔧 Future Improvements

- Add confidence score (similarity %).
- Show top auto-suggestion.
- Support multiple datasets (e.g., animals, cities).

---

## 🧾 License

This project is **open source** under the MIT License.
