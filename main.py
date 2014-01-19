""" main.py is the top level script.

Return "Hello World" at the root URL.
"""

import os
import sys

# sys.path includes 'server/lib' due to appengine_config.py
from flask import Flask
from flask import render_template
app = Flask(__name__.split('.')[0])

from instagram.client import InstagramAPI
from random import choice

@app.route('/')
@app.route('/<name>')
def hello(name=None):
  """ Return hello template at application root URL."""
  # TODO: Move to environment variable
  access_token = "995294683.26174be.94f2626419534650812cf5ed542d5a9d"
  api = InstagramAPI(access_token=access_token)
  pickles, next = api.tag_recent_media(10, 0, "pickle")

  # TODO: Better pickle selection, reduce duplicates
  choice_pickle = choice(pickles)
  # Truncate long captions
  pickle_caption = choice_pickle.caption.text.lower()
  pickle_caption = (pickle_caption[:110] + "...") if len(pickle_caption) > 110 else pickle_caption

  pickle_link = choice_pickle.link
  pickle_user = choice_pickle.user.username
  pickle_image_link = choice_pickle.images["standard_resolution"].url

  # TODO: Download generated image with canvas
  # TODO: Post the best ones to a an instagram account or tweet them.

  return render_template('hello.html', caption=pickle_caption, username=pickle_user, link=pickle_link, image=pickle_image_link)


