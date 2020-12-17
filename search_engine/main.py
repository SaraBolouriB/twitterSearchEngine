import xlsxwriter
from getTextTweets import textTweets
from preProcessing import preprocess
from tweetInformation import profile_info

dataset = "../dataset/test.csv"

def print_clean_data(cleanTweetText):
    '''
        1. Saved data in excel file witch was named "cleanTextOutput.xlsx"
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


def print_user_behavior(user_behavior):
    workbook = xlsxwriter.Workbook('user_behavior.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    worksheet.write(row, col, "Tweet ID")
    worksheet.write(row, col + 1, "User ID")
    worksheet.write(row, col + 2, "Username")
    worksheet.write(row, col + 3, "Screen Name")
    worksheet.write(row, col + 4, "User Location")
    worksheet.write(row, col + 5, "Followers Count")
    worksheet.write(row, col + 6, "Created at")
    worksheet.write(row, col + 7, "User Tweet Count")
    worksheet.write(row, col + 8, "Tweet Like")
    worksheet.write(row, col + 9, "Retweet Count")
    row += 1
    for user in user_behavior:
        worksheet.write(row, col, user['tweet_id'])
        worksheet.write(row, col + 1, user["user_id"])
        worksheet.write(row, col + 2, user["user_name"])
        worksheet.write(row, col + 3, user["screen_name"])
        worksheet.write(row, col + 4, user["user_location"])
        worksheet.write(row, col + 5, user["followers_count"])
        worksheet.write(row, col + 6, user["account_created_at"])
        worksheet.write(row, col + 7, user["tweets_count"])
        worksheet.write(row, col + 8, user["favorite_count"])
        worksheet.write(row, col + 9, user["retweet_count"])

        row += 1
    workbook.close()

## the program start here!
if __name__ == '__main__':
    allTweetTexts = textTweets(dataset)
    cleanTweetText = preprocess(allTweetTexts)
    print_clean_data(cleanTweetText)
    user_behavior = profile_info()
    print_user_behavior(user_behavior)