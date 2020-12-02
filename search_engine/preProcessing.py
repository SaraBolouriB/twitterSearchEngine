import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import re
import string
import preprocessor as p
from spellchecker import SpellChecker

a = [{"tweetId" : "123", "tweetText" : "She became herre but (no one) is thrre there was a good dayyyy"}]


# Reducing Length
def reduce_lengthening(text):
    pattern = re.compile(r"(.)\1{2,}")
    return pattern.sub(r"\1\1", text)

# Correct Misspelling
def correction_sent(text):
    spell = SpellChecker()
    splitted_sentence = text.split(" ")[:-1]
    sentence = ""
    for word in splitted_sentence:
        sentence += spell.correction(word) + " "
    return sentence



def preprocess(tweetText):
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    stopWords = set(stopwords.words('english'))
    snowballStemmer = SnowballStemmer('english')

    for tweet_text in tweetText:
        cleanTweet = re.sub(r'\d+', '', tweet_text["tweetText"])                            # Remove Numbers
        cleanTweet = cleanTweet.lower()                                                     # Convert To LowerCase
        cleanTweet = p.clean(cleanTweet)                                                    # Remove urls, mentions
        cleanTweet = cleanTweet.translate(str.maketrans(dict.fromkeys(string.punctuation))) # Remove (, ), +, %, *, =, /
        cleanTweet = reduce_lengthening(cleanTweet)                                         # Reduce Length
        cleanTweet = correction_sent(cleanTweet)                                            # Correct misspellings
        cleanTweet = tokenizer.tokenize(cleanTweet)                                         # Tokenize Each String
        cleanTweet = [w for w in cleanTweet if w not in stopWords]                          # Remove Stop Words
        cleanTweet = [snowballStemmer.stem(word) for word in cleanTweet]                    # Stemming

        print(f"tweetID {tweet_text['tweetId']}: {str(cleanTweet)}")



preprocess(a)
