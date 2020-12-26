from secret import api
import tweepy
from getTextTweets import all_user_id

user_profile = []
timeline = []
total_timeline = []

def profile_info():
    '''
        Get status object with tweepy API.
        Status Object was used to fetch user profile information.
    '''
    for user in all_user_id:
        try:
            status = api.get_status(int(user['tweetId']))
            user_profile.append({
                "tweet_id": user['tweetId'],
                "user_id": status.user.id,
                "user_name": status.user.name,
                "screen_name": status.user.screen_name,
                "user_location": status.user.location,
                "followers_count": status.user.followers_count,
                "account_created_at": status.user.created_at,
                "tweets_count": status.user.statuses_count,
                "favorite_count": status.favorite_count,
                "retweet_count": status.retweet_count,
            })
            get_user_Tweets(user, status.user.screen_name)
        except:
            user_profile.append({
                "tweet_id": user['tweetId'],
                "user_id": "Not Found!",
                "user_name": "Not Found!",
                "screen_name": "Not Found!",
                "user_location": "Not Found!",
                "followers_count": "Not Found!",
                "account_created_at": "Not Found!",
                "tweets_count": "Not Found!",
                "favorite_count": "Not Found!",
                "retweet_count": "Not Found!",
            })
    return user_profile, total_timeline

def get_user_Tweets(user, screen_name):
    '''
        Get five last tweets of user whose name is keeping in screen_name variable.
    '''
    i = 1
    for status in tweepy.Cursor(api.user_timeline, screen_name=screen_name).items(5):
        timeline.append({f"timeline{i}":status.text})
        i += 1
    total_timeline.append({
        "tweet_id": user['tweetId'],
        "timeline1": timeline[0],
        "timeline2": timeline[1],
        "timeline3": timeline[2],
        "timeline4": timeline[3],
        "timeline5": timeline[4],
    })
    timeline.clear()
