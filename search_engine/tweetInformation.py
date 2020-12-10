from secret import api

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



