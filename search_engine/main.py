from getTextTweets import textTweets
from preProcessing import preprocess

dataset = "../dataset/test.csv"


## the program start here!
if __name__ == '__main__':
    print("Text of Tweet are below:")
    allTweetTexts = textTweets(dataset)
    preprocess(allTweetTexts)