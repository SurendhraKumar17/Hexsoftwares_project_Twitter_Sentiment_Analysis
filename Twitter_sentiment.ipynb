{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "61a07a15-455a-4d41-a984-35ce81d37a4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Loading data from /Users/surendhrakumarnunna/Documents/test_tweets.csv...\n",
      "Analyzing 17197 tweets in the 'tweet' column...\n",
      "\n",
      "=============================================\n",
      "FINAL SENTIMENT ANALYSIS SUMMARY\n",
      "=============================================\n",
      "Total Tweets Analyzed: 17,197\n",
      "-------------------------\n",
      "Positive  :  48% (8,419)\n",
      "Negative  :  13% (2,340)\n",
      "Neutral   :  37% (6,438)\n",
      "-------------------------\n",
      "Overall Polarity Score: 0.1713\n",
      "Conclusion: The final sentiment analyasis of tweet is POSITIVE. 👍🏻\n",
      "=============================================\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from textblob import TextBlob\n",
    "import re\n",
    "\n",
    "FILE_PATH = '/Users/surendhrakumarnunna/Documents/test_tweets.csv'\n",
    "TEXT_COLUMN = 'tweet'\n",
    "DATA_ENCODING = 'latin1'\n",
    "\n",
    "def clean_text(text):\n",
    "    text = str(text)\n",
    "    text = re.sub(r'@\\w+', '', text)\n",
    "    text = text.replace('RT', '').strip()\n",
    "    return text\n",
    "\n",
    "def get_sentiment_category(polarity):\n",
    "    if polarity > 0.05:\n",
    "        return 'Positive'\n",
    "    elif polarity < -0.05:\n",
    "        return 'Negative'\n",
    "    return 'Neutral'\n",
    "\n",
    "def analyze_sentiment_from_csv(file_path, text_column, encoding):\n",
    "    print(f\"Loading data from {file_path}...\")\n",
    "    try:\n",
    "        df = pd.read_csv(file_path, encoding=encoding, usecols=['id', text_column])\n",
    "    except Exception as e:\n",
    "        print(f\"Error loading file: {e}\")\n",
    "        return\n",
    "\n",
    "    print(f\"Analyzing {len(df)} tweets in the '{text_column}' column...\")\n",
    "\n",
    "    df['clean_tweet'] = df[text_column].apply(clean_text)\n",
    "    df['polarity_score'] = df['clean_tweet'].apply(lambda x: TextBlob(x).sentiment.polarity)\n",
    "    df['sentiment'] = df['polarity_score'].apply(get_sentiment_category)\n",
    "\n",
    "    sentiment_counts = df['sentiment'].value_counts(normalize=True) * 100\n",
    "    total_count = len(df)\n",
    "    avg_polarity = df['polarity_score'].mean()\n",
    "\n",
    "    print(\"\\n\" + \"=\"*45)\n",
    "    print(\"FINAL SENTIMENT ANALYSIS SUMMARY\")\n",
    "    print(\"=\"*45)\n",
    "    print(f\"Total Tweets Analyzed: {total_count:,}\")\n",
    "    print(\"-\" * 25)\n",
    "    \n",
    "    for category in ['Positive', 'Negative', 'Neutral']:\n",
    "        percentage = sentiment_counts.get(category, 0)\n",
    "        print(f\"{category:<10}: {int(percentage):>3}% ({df['sentiment'].value_counts().get(category, 0):,})\")\n",
    "\n",
    "    print(\"-\" * 25)\n",
    "    print(f\"Overall Polarity Score: {avg_polarity:.4f}\")\n",
    "\n",
    "    if avg_polarity > 0.05:\n",
    "        print(\"Conclusion: The final sentiment analyasis of tweet is POSITIVE. 👍🏻\")\n",
    "    elif avg_polarity < -0.05:\n",
    "        print(\"Conclusion: The final sentiment analyasis of tweet is NEGATIVE. 👎🏻\")\n",
    "    else:\n",
    "        print(\"Conclusion: The overall sentiment is NEUTRAL. ⚖️\")\n",
    "    print(\"=\"*45)\n",
    "\n",
    "analyze_sentiment_from_csv(FILE_PATH, TEXT_COLUMN, DATA_ENCODING)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "230d7b1e-9a51-4be1-bd8c-551e62a92d41",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
