# Fake News Detection

A Machine Learning project that predicts whether a news article is **Fake** or **Real** using Natural Language Processing (NLP).

## Technologies Used

* Python
* Pandas
* Scikit-learn
* NLTK
* TF-IDF
* Logistic Regression
* Streamlit

## Dataset

The dataset contains news articles with two labels:

* `FAKE`
* `REAL`

The project uses the **title** and **text** of the news article.

## Data Preprocessing

The following preprocessing steps were performed:

1. Removed unnecessary columns
2. Combined title and text
3. Converted text to lowercase
4. Removed punctuation
5. Removed stopwords
6. Applied stemming
7. Converted text into numerical features using TF-IDF

## Model

A **Logistic Regression** model was trained for classification.

### Performance

* Accuracy: **90.12%**

## Confusion Matrix

```text
[[31, 4],
 [4, 42]]
```

## How to Run

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

## Project Files

```text
Fake-News-Detection/
│
├── app.py
├── model.pkl
├── tfidf.pkl
├── requirements.txt
├── .gitignore
└── README.md
```
