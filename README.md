# 🐦 Tweet Sentiment Analysis

This project performs **sentiment analysis on tweets** using Python, **pandas**, and **TextBlob**.  
It reads tweets from a CSV file, cleans them, calculates sentiment polarity, and classifies each tweet as **Positive**, **Negative**, or **Neutral**.

---

## 📊 Features

- Cleans tweet text (removes mentions, RTs, etc.)
- Analyzes sentiment using **TextBlob**
- Categorizes tweets into Positive / Negative / Neutral
- Displays summary statistics and overall sentiment conclusion

---

## 🧰 Requirements

- Python 3.8+
- The following Python libraries:
  - pandas
  - textblob

## Upload Web App

The repository also includes `app.py`, a Streamlit interface for uploading TXT,
Markdown, CSV, TSV, JSON, Excel, PDF, and Word files. It displays Positive,
Neutral, and Negative totals, a chart, polarity scores, and detailed results.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Open https://share.streamlit.io/.
2. Select this repository and the `main` branch.
3. Set the main file to `app.py`.
4. Deploy.



