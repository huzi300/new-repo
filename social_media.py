import tweepy

def initialize_twitter_api(api_key, api_key_secret, access_token, access_token_secret):
    try:
        auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
        return tweepy.API(auth)
    except Exception as e:
        return str(e)

def post_tweet(api, message):
    try:
        api.update_status(message)
        return "Tweet posted successfully."
    except Exception as e:
        return str(e)
