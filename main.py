import tweepy

from config import access


def main():

    f = open('last_checked.txt', 'r')
    sid = f.read()
    old_last_id = int(sid)
    f.close()

    ckey = access['consumer_key']
    csecret = access['consumer_secret']
    tkey = access['access_token_key']
    tsecret = access['access_token_secret']

    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(tkey, tsecret)

    api = tweepy.API(auth)
    tweets = api.home_timeline(since_id=sid)

    if tweets:
        last_checked_id = tweets[0].id
        f = open('last_checked.txt', 'w')
        f.write(str(last_checked_id))
        f.close()

    api.update_status('Test! From Heroku!')


if __name__ == '__main__':
    main()
