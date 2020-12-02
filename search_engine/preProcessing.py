import nltk
import re
import string
import preprocessor as p
# from pattern.en import spelling
from spellchecker import SpellChecker

a = [{"tweetId" : "123", "tweetText" : "Hiiiiiii (thwer@ m+sy 12 %name)) //======i+s sara **"}]


# Correcting Word By Reducing Length
def reduce_lengthening(text):
    pattern = re.compile(r"(.)\1{2,}")
    return pattern.sub(r"\1\1", text)

def correction_sent(text):
    spell = SpellChecker()
    splitted_sentence = text.split(" ")[:-1]
    sentence = ""
    for word in splitted_sentence:
        sentence += spell.correction(word) + " "
    return sentence



def preprocess(tweetText):
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    

    for tweet_text in tweetText:
        cleanTweet = re.sub(r'\d+', '', tweet_text["tweetText"])                            # Remove Numbers
        cleanTweet = cleanTweet.lower()                                                     # Convert To LowerCase
        cleanTweet = p.clean(cleanTweet)                                                    # Remove urls, mentions
        cleanTweet = cleanTweet.translate(str.maketrans(dict.fromkeys(string.punctuation))) # Remove (, ), +, %, *, =, /
        cleanTweet = reduce_lengthening(cleanTweet)                                         # Reduce Length
        cleanTweet = correction_sent(cleanTweet)                                            # Correct misspelling
        cleanTweet = tokenizer.tokenize(cleanTweet)                                         # Tokenize Each String
        print(f"tweetID {tweet_text['tweetId']}: {cleanTweet}")



preprocess(a)
