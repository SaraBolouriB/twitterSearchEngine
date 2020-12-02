import re
import preprocessor as p

def preprocess(tweetText):
    tokenizer = nltk.RegexpTokenizer(r"\w+")

    for tweet_text in tweetText:
        cleanTweet = re.sub(r'\d+', '', tweetText["tweetText"]) # Remove Numbers
        cleanTweet = tweet_text["tweetText"].lower()            # Convert To LowerCase
        cleanTweet = p.clean(cleanTweet)                        # Remove @, url, ..
        print(f"tweetID {tweet_text['tweetId']}: {cleanTweet}")



