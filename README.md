#  Tweet Sentiment Analyzer

This project is a **Twitter (X) Sentiment Analyzer** that scrapes real-time tweets based on a given search query, performs sentiment analysis, and visualizes the results. Using **Selenium**, the script dynamically fetches tweets, processes them using a **custom sentiment analysis algorithm**, and categorizes them as **Positive, Negative, or Neutral**.

---

##  Features

 Scrapes live tweets from Twitter (X)  
 Custom sentiment analysis algorithm (rule-based)  
 Dynamic scrolling to fetch large datasets (e.g., 1500 tweets)  
 Avoids duplicate tweets for better accuracy  
 Generates sentiment reports & visual graphs  

---

##  Installation

Make sure you have **Python 3.8+** installed.

###  Clone the repository  
```bash
git clone https://github.com/aozkurt/TweetSentimentAnalyzer.git
cd TweetSentimentAnalyzer
```

## Install Dependencies
```bash
pip install undetected-chromedriver selenium matplotlib
```

## Requirements

- undetected-chromedriver (for bypassing bot detection)
- selenium (for web scraping)
- matplotlib (for visualizing sentiment analysis results)


## Sentiment Analysis Results:

 Positive Tweets: 35<br>
 Negative Tweets: 40<br>
 Neutral Tweets: 25
