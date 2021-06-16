from flask import Flask
from flask_restful import Api
from resources import Tweet, Comments
import logging


# App and API Declarations
app = Flask(__name__)
api = Api(app, prefix="/api/v1")
api.add_resource(Tweet, '/tweet/<tweet_id>')
api.add_resource(Comments, '/comments/<tweet_id>')
api.app.config['RESTFUL_JSON'] = {'ensure_ascii': False}

# logger
logging.basicConfig(filename='twitter_unofficial_api.log', level=logging.DEBUG)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)  # localhost
