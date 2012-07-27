import soundcloud
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://angelo:ciaobella@localhost/trip2'
db = SQLAlchemy(app)

SOUNDCLOUD_CLIENT_ID = ''
SOUNDCLOUD_CLIENT_SECRET = ''
SOUNDCLOUD_REDIRECT_URL = ''


class SoundcloudConnector(object):
    redirect_url = None

    def __init__(self):
        # create client object with app credentials
        client = soundcloud.Client(client_id=SOUNDCLOUD_CLIENT_ID,
                                   client_secret=SOUNDCLOUD_CLIENT_SECRET,
                                   redirect_uri=SOUNDCLOUD_REDIRECT_URL)

        # redirect user to authorize URL
        self.redirect_url = client.authorize_url()
