import nltk
import re
import string
import preprocessor as p

a = [{"tweetId" : "123", "tweetText" : "Hi (thwer@ m+sy 12 %name)) //======i+s sara **"}]

def preprocess(tweetText):
    tokenizer = nltk.RegexpTokenizer(r"\w+")

    for tweet_text in tweetText:
        cleanTweet = re.sub(r'\d+', '', tweet_text["tweetText"])                            # Remove Numbers
        cleanTweet = cleanTweet.lower()                                                     # Convert To LowerCase
        cleanTweet = p.clean(cleanTweet)                                                    # Remove urls, mentions
        cleanTweet = cleanTweet.translate(str.maketrans(dict.fromkeys(string.punctuation))) # Remove (, ), +, %, *, =, /
        cleanTweet = tokenizer.tokenize(cleanTweet)                                         # Tokenize Each String
        print(f"tweetID {tweet_text['tweetId']}: {cleanTweet}")



preprocess(a)