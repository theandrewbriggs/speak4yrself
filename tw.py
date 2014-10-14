import tweepy

from config import access


def main():

    ckey = access['consumer_key']
    csecret = access['consumer_secret']
    tkey = access['access_token_key']
    tsecret = access['access_token_secret']

    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(tkey, tsecret)

    api = tweepy.API(auth)
    api.update_status('test! hi.')

if __name__ == '__main__':
    main()
