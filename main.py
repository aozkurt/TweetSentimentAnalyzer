import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import matplotlib.pyplot as plt

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

options = uc.ChromeOptions()

profile = "C:\\Users\\Pc\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
options.add_argument(f"user-data-dir={profile}")

driver = uc.Chrome(options=options, use_subprocess=True)

#Link
driver.get(
    "https://x.com/search?q='Bitcoin'%20'BTC'%20lang%3Aen%20-filter%3Alinks%20-filter%3Areplies&src=recent_search_click")

# If the login screen appears, uncomment the line below and run the script.
# After logging in, close the tab, then comment the line again and rerun the script.
# time.sleep(10000)
time.sleep(4)

wait = WebDriverWait(driver, 5)
tweet_texts = set()
tweet_limit = 15

def scroll_down():
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

while len(tweet_texts) < tweet_limit:
    tweet_containers = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-testid='cellInnerDiv']"))
    )

    for tweet in tweet_containers:
        try:
            tweet_text_elements = tweet.find_elements(By.XPATH, ".//span")
            tweet_text = " ".join(span.text for span in tweet_text_elements if span.text.strip())

            if tweet_text and tweet_text not in tweet_texts:
                tweet_texts.add(tweet_text)

        except Exception as e:
            print(f"Error extracting tweet: {e}")
            continue

    scroll_down()

driver.quit()

tweet_list = list(tweet_texts)

sentiment_results = []
for tweet in tweet_list:
    sentiment_score = sia.polarity_scores(tweet)
    compound = sentiment_score["compound"]

    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    sentiment_results.append({"tweet": tweet, "sentiment": sentiment, "score": compound})

positive = sum(1 for result in sentiment_results if result["sentiment"] == "Positive")
negative = sum(1 for result in sentiment_results if result["sentiment"] == "Negative")
neutral = sum(1 for result in sentiment_results if result["sentiment"] == "Neutral")


for result in sentiment_results[:3]:
    print(f"\nTweet: {result['tweet']}\nSentiment: {result['sentiment']} (Score: {result['score']})")

print(f"\n Sentiment Analysis Results:\n")
print(f" Positive Tweets: {positive}")
print(f" Negative Tweets: {negative}")
print(f" Neutral Tweets: {neutral}")

sentiment_counts = {"Positive": positive, "Neutral": neutral, "Negative": negative}

labels = list(sentiment_counts.keys())
values = list(sentiment_counts.values())

plt.figure(figsize=(6,4))
plt.bar(labels, values, color=['green', 'gray', 'red'])
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.title("Sentiment Analysis of Tweets")

plt.show()