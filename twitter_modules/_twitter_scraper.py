import requests
from ._twitter_auth import TwitterAuth


class TweetScraper:
    __BASE_TWEET_URL = "https://twitter.com/i/api/2/timeline/conversation/"

    def __init__(self):
        self.headers = {
            "Authorization": TwitterAuth.auth_header(),
            "x-guest-token": TwitterAuth.refresh_token()
        }
        self.cookies = TwitterAuth.get_base_cookies()

    def get_tweet_data(self, tweet_id):
        """
        gets tweets and comment raw JSON data
        :param tweet_id: tweet id
        :return: raw JSON data from unofficial API tweet and comments
        """

        url = f"{self.__BASE_TWEET_URL}{tweet_id}.json"
        params = {"tweet_mode": "extended",
                  "cursor": "LBlGrICz9czh9v0mjMC5paGEjv4mgMCrxaS/9P0mgsC4/Y6l9v0mJQQRAAA="}
        r = requests.get(url, headers=self.headers, cookies=self.cookies, params=params)
        if not r.ok:  # Refreshing token
            self.headers["x-guest-token"] = TwitterAuth.refresh_token()
            r = requests.get(url, headers=self.headers, cookies=self.cookies, params=params)
        if r.status_code == 404:
            return None
        return r.json()['globalObjects'].get('tweets')

    def get_tweet(self, tweet_id):
        """
        gets tweets JSON from unofficial API
        :param tweet_id: tweet_id
        :return: tweet raw JSON data
        """

        response_json = self.get_tweet_data(tweet_id)
        if response_json is None:
            return None
        tweet_json = response_json.get(tweet_id)
        return tweet_json

    def get_comments(self, tweet_id):
        """
        gets comments JSON from unofficial API
        :param tweet_id: tweet_id
        :return: comments raw JSON data
        """

        response_json = self.get_tweet_data(tweet_id)
        if response_json is None:
            return None
        response_json.pop(tweet_id)
        return [tweet_json for tweet_json in response_json.values()]
