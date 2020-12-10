import xlsxwriter
from getTextTweets import textTweets
from preProcessing import preprocess

dataset = "../dataset/test.csv"

def print_clean_data(cleanTweetText):
    '''
        1. Saved data in excel file wiche was named "cleanTextOutput.xlsx"
        2. Print clean text
    '''
    workbook = xlsxwriter.Workbook('cleanTextOutput.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    worksheet.write(row, col, "Tweet ID")
    worksheet.write(row, col + 1, "Tweet Text")
    worksheet.write(row, col + 2, "Cleaned Tweet Text")
    row += 1
    print("Body of Tweet are below:")
    for tweet in cleanTweetText:
        worksheet.write(row, col, tweet['tweetId'])
        worksheet.write(row, col + 1, tweet["tweetText"])
        worksheet.write_row(row, col + 2, tweet["tweetClean"])
        row += 1
        print(f"TweetID: {tweet['tweetId']}\nOrginalTweet: {tweet['tweetText']}\nCleanTweet: {tweet['tweetClean']}\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    workbook.close()

## the program start here!
if __name__ == '__main__':
    allTweetTexts = textTweets(dataset)
    cleanTweetText = preprocess(allTweetTexts)
    print_clean_data(cleanTweetText)