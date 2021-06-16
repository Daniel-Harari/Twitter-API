from twitter_modules import TweetScraper


class TweetModel:
    scraper = TweetScraper()

    @staticmethod
    def _tweet_json(tweet):
        """
        creates a JSON containing relevant data of tweet
        :param tweet: JSON of tweet from unofficial API
        :return: JSON repr of tweet
        """
        return {
            "tweet_id": tweet["id_str"],
            "data": {
                "text": tweet["full_text"],
                "tweeter_id": tweet["user_id_str"],
                "date": tweet["created_at"],
                "retweets": tweet["retweet_count"],
                "likes": tweet["favorite_count"],
            }
        }

    @classmethod
    def get_tweet_json(cls, tweet_id):
        """

        :param tweet_id: tweet id
        :return: JSON repr of tweet id
        """
        tweet = cls.scraper.get_tweet(tweet_id)
        if tweet is None:
            return None
        return cls._tweet_json(tweet)

    @classmethod
    def get_comments_json(cls, tweet_id):
        """
        :param tweet_id: tweet id
        :return: JSON repr of comments as JSON array
        """
        tweet_lst = cls.scraper.get_comments(tweet_id)
        if tweet_lst is None:
            return None
        return {'comment_data': [cls._tweet_json(tweet) for tweet in tweet_lst]}
