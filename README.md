**ReadabilityLola – Local Language Readability Scoring**

📌 **Overview**

ReadabilityLola is a Python library to compute readability scores for local languages, currently supporting Bahasa and Hindi. The goal is to provide metrics that help evaluate the ease of reading texts in languages where readability research is limited.

Readability measures how easy a text is to understand. High readability allows readers to process sentences quickly and effortlessly, while low readability increases cognitive load due to complex sentence structures or difficult vocabulary.

⚙️ **Installation**
```bash
pip install readabilitylola
```

⚙️ **Features**

- Compute **readability scores** for local languages, currently supporting **Bahasa** and **Hindi**.
- Easy-to-use **Python API** for text analysis
- Modular and reusable code suitable for **research or linguistic analysis**

💡 **Usage Example**
```python
from readabilitylola import ReadabilityLola


text = "Your sample text here"
score = ReadabilityLola(language='Bahasa').compute(text)
print(f"Readability score: {score}")

```
## 🧮 Readability Formulas

### Bahasa
```math

Score = -13.988 + 0.3793 × (300 / S) + 0.0207 × (d + k)

```

**Where:**  
- **S** = Number of sentences in 300 words  
- **d** = Number of syllables  
- **k** = Number of potentially difficult words:  

`k = 5 × (Kata Ganda + Diftong + Kata Pinjaman + Kekeliruan Huruf)`

**Bahasa formula** considers:
  - Sentence length
  - Number of syllables
  - Difficult words, including:
    - Kata Ganda
    - Diftong
    - Kata Pinjaman
    - Kekeliruan Huruf


### Hindi

```math

Score = -2.34 + 2.14 × AWL + 0.01 × PSW
```

**Hindi formula** considers:
  - Average word length (AWL)
  - Poly-syllabic words (PSW: words with more than 2 syllables)


📌 Notes

Readability formulas are heuristic-based; accuracy may vary across texts.

Currently supports Bahasa and Hindi; formulas for other languages are research topics.

Useful for linguistic analysis, content optimization, and readability research.

✅ Skills Highlighted

Python (library development, modular design)

Text analysis & NLP basics (tokenization, syllable counting, difficult word detection)

Cross-linguistic application of computational metrics

Clean documentation suitable for portfolio / research submission
