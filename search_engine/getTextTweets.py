from secret import api
import csv

all_user_id = []

def reader(address):
    '''
        1. read rows of .scv file which contains tweeterID, sarcasm_label and sarcasm_type.
        2. saved just tweeterID in "all_user_id" list
        3. return "all_user_id"
    '''

    with open(address, 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for user_id in csv_reader:
            all_user_id.append({"tweetId" : user_id[0]})
    
    return all_user_id

def textTweets(dataset_add):
    '''
        1. get all tweeterID by reader() method
        2. for each tweeterID if there is a text tweet we print it otherwise we printed "Not Found"
    '''
    allTextTweet = []
    all_user_id = reader(dataset_add)
    all_user_id.pop(0)
    for user_id in all_user_id:
        try:
            status = api.get_status(user_id["tweetId"])
            allTextTweet.append({"tweetId": user_id["tweetId"],"tweetText": status.text})
            # print(f"tweetID {user_id['tweetId']}: {status.text}")
        except:
            print(f"tweetID {user_id['tweetId']} Not Found!")
            continue

    return allTextTweet
