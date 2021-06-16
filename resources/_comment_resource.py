from flask_restful import Resource
from models import TweetModel


class Comments(Resource):
    """
    public comments resource
    """

    @staticmethod
    def get(tweet_id):
        try:
            comments_json = TweetModel.get_comments_json(tweet_id)
        except Exception as e:
            print(e)
            return {"msg": "somthing went wrong"}, 500
        if comments_json is None:
            return {"msg": "tweet_id doesn't exist"}, 404
        return comments_json, 200
