from flask_restful import Resource
from models import TweetModel


class Tweet(Resource):
    """
    public tweet resource
    """

    @staticmethod
    def get(tweet_id):
        try:
            tweet_json = TweetModel.get_tweet_json(tweet_id)
        except Exception as e:
            print(e)
            return {"msg": "somthing went wrong"}, 500
        if tweet_json is None:
            return {"msg": "tweet_id doesn't exist"}, 404
        return tweet_json, 200
