from secret import api
import tweepy
from getTextTweets import all_user_id

user_profile = []

def profile_info():
    '''
        Get status object with tweepy API.
        Status Object was used to fetch user profile information.
    '''
    for user in all_user_id:
        try:
            status = api.get_status(int(user['tweetId']))
            user_profile.append({"tweet_id": user['tweetId'],"user_id": status.user.id,"user_name": status.user.name,"screen_name": status.user.screen_name,"user_location": status.user.location,"followers_count": status.user.followers_count,"account_created_at": status.user.created_at,"tweets_count": status.user.statuses_count,"favorite_count": status.favorite_count,"retweet_count": status.retweet_count})
        except:
            user_profile.append({"tweet_id": user['tweetId'],"user_id": "Not Found!","user_name": "Not Found!","screen_name": "Not Found!","user_location": "Not Found!","followers_count": "Not Found!","account_created_at": "Not Found!","tweets_count": "Not Found!","favorite_count": "Not Found!","retweet_count": "Not Found!"})
    return(user_profile)

def get_userTweets(username):
    '''
        Get five last tweets of user whose name is keeping in screen_name variable.
    '''
    i = 1
    for status in tweepy.Cursor(api.user_timeline, screen_name=username).items(5):
        user_profile.append({
            "time_line_" + str(i): status.text
        })
        i = i + 1