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
    workbook = xlsxwriter.Workbook('./Output/cleanTextOutput.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    worksheet.write(row, col, "Tweet ID")
    worksheet.write(row, col + 1, "Tweet Text")
    worksheet.write(row, col + 2, "Cleaned Tweet Text")
    row += 1
    for tweet in cleanTweetText:
        worksheet.write(row, col, tweet['tweetId'])
        worksheet.write(row, col + 1, tweet["tweetText"])
        worksheet.write_row(row, col + 2, tweet["tweetClean"])
        row += 1
        print(
            f"TweetID: {tweet['tweetId']}\nOrginalTweet: {tweet['tweetText']}\nCleanTweet: {tweet['tweetClean']}\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    workbook.close()


def print_user_behavior(user_behavior, user_timeline):

    workbook = xlsxwriter.Workbook('./Output/user_behavior.xlsx')
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
    index = 0
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
        print(f"Tweet Id: {user['tweet_id']}\nUser Id: {user['user_id']}\nUsername: {user['user_name']}\nScreen Name: {user['screen_name']}\nLocation: {user['user_location']}\nFollowers Count: {user['followers_count']}\nAccount Created At: {user['account_created_at']}\nUser Tweet Count: {user['tweets_count']}\nTweet Like: {user['favorite_count']}\nRetweet Count: {user['retweet_count']}")
        timeline = user_timeline[index]
        if timeline['tweet_id'] == user['tweet_id']:
            print(f"Tweet Id: {timeline['tweet_id']}\nTimeline 1: {timeline['timeline1']['timeline1']}\nTimeline 2: {timeline['timeline2']['timeline2']}\nTimeline 3: {timeline['timeline3']['timeline3']}\nTimeline 4: {timeline['timeline4']['timeline4']}\nTimeline 5: {timeline['timeline5']['timeline5']}")
            index += 1
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    workbook.close()


def print_user_timeline(user_timeline):
    workbook = xlsxwriter.Workbook('./Output/user_timeline.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    worksheet.write(row, col, "Tweet ID")
    worksheet.write(row, col + 1, "TimeLine 1")
    worksheet.write(row, col + 2, "TimeLine 2")
    worksheet.write(row, col + 3, "TimeLine 3")
    worksheet.write(row, col + 4, "TimeLine 4")
    worksheet.write(row, col + 5, "TimeLine 5")
    row += 1
    for user in user_timeline:
        worksheet.write(row, col, user['tweet_id'])
        worksheet.write(row, col + 1, user['timeline1']['timeline1'])
        worksheet.write(row, col + 2, user['timeline2']['timeline2'])
        worksheet.write(row, col + 3, user['timeline3']['timeline3'])
        worksheet.write(row, col + 4, user['timeline4']['timeline4'])
        worksheet.write(row, col + 5, user['timeline5']['timeline5'])
        row += 1
        # print(f"Tweet Id: {user['tweet_id']}\nTimeline 1: {user['timeline1']['timeline1']}\nTimeline 2: {user['timeline2']['timeline2']}\nTimeline 3: {user['timeline3']['timeline3']}\nTimeline 4: {user['timeline4']['timeline4']}\nTimeline 5: {user['timeline5']['timeline5']}\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    workbook.close()


## the program start here!
if __name__ == '__main__':
    allTweetTexts = textTweets(dataset)
    cleanTweetText = preprocess(allTweetTexts)
    print("*************************************** Phase 2 ***************************************")
    print_clean_data(cleanTweetText)
    user_behavior = profile_info()
    print("*************************************** Phase 3 ***************************************")
    print("*************************************** User Behavior ***************************************")
    print_user_behavior(user_behavior[0],user_behavior[1])
    # print("*************************************** User Timeline ***************************************")
    print_user_timeline(user_behavior[1])
