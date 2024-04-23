import tweepy
from textblob import TextBlob
from flask import Flask, request, render_template

consumer_key = 'juliusottode'
consumer_secret = 'sdagf5464f6g'
access_token = '78932185'
access_token_secret = '823687168'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic = request.form['topic']
        public_tweets = api.search_tweets(q=topic, count=10, tweet_mode='extended')
        sentiment_results = []
        for tweet in public_tweets:
            analysis = TextBlob(tweet.full_text)
            sentiment_results.append((tweet.full_text, analysis.sentiment))
        return render_template('results.html', sentiments=sentiment_results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
