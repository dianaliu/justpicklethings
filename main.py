import os
import sys

# sys.path includes 'server/lib' due to appengine_config.py
from flask import Flask
from flask import render_template
app = Flask(__name__.split('.')[0])

from instagram.client import InstagramAPI
import random
from random import choice

@app.route('/')
def index():
  # TODO: Move to environment variable
  access_token = "995294683.26174be.94f2626419534650812cf5ed542d5a9d"
  api = InstagramAPI(access_token=access_token)

  # Get 30 pickles starting at a random page
  num = 30
  page = random.randint(0, 10)
  pickles, next = api.tag_recent_media(num, page, "pickle")

  choice_pickle = choice(pickles)

  # Truncate long captions
  pickle_caption = choice_pickle.caption.text.lower()
  pickle_caption = (pickle_caption[:110] + "...") if len(pickle_caption) > 110 else pickle_caption

  pickle_link = choice_pickle.link
  pickle_user = choice_pickle.user.username
  if hasattr(choice_pickle, "images"):
    pickle_image_link = choice_pickle.images["standard_resolution"].url
  elif hasattr(choice_pickle, "videos"):
    # FIXME: Update template
    pickle_image_link = choice_pickle.videos["standard_resolution"].url

  # TODO: Download generated image with canvas
  # TODO: Post the best ones to a an instagram account or tweet them.

  return render_template('index.html', caption=pickle_caption, username=pickle_user, link=pickle_link, image=pickle_image_link)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('error.html'), 404
