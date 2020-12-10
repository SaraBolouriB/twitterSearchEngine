from secret import api
import tweepy

def profile_info(tweetID):
    '''
        Get status object with tweepy API.
        Status Object was used to fetch user profile information.
    '''
    status = api.get_status(int(tweetID))
    user_profile = {
        "user_id" : status.user.id,
        "user_name" : status.user.name,
        "screen_name" : status.user.screen_name,
        "user_location" : status.user.location,
        "followers_count" : status.user.followers_count,
        "account_created_at" : status.user.created_at,
        "tweets_conunt" : status.user.statuses_count
    }
    return(user_profile)

def get_userTweets(username):
    '''
        Get five last tweets of user whose name is keeping in screen_name variable.
    '''
    for status in tweepy.Cursor(api.user_timeline, screen_name=username).items(5):
        print(status.text)