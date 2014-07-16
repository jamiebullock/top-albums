import os
from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
import pylast

from app_private import *

app = Flask(__name__)

class Album:
    title = ""
    artist = ""
    link = ""


network = pylast.LastFMNetwork(api_key = LASTFM_API_KEY, api_secret = LASTFM_SECRET)

def get_albums_for_user(username):
    user = network.get_user(username)
    lastfm_albums = user.get_top_albums(period=pylast.PERIOD_12MONTHS)

    albums = []

    for lastfm_album in lastfm_albums[:10]:
        album = Album()
        album.title = lastfm_album.item.get_title()
        album.artist = lastfm_album.item.get_artist().name
        album.link = lastfm_album.item.get_url()
        albums.append(album)

    return albums

@app.route('/', methods=['POST', 'GET'])
def get_user():
    if request.method == 'POST':
        page = redirect(url_for('list_albums', username=request.form['user']))
    else:
        page = render_template('index.html')
    return page

@app.route('/albums/<username>')
def list_albums(username):
    try:
        albums = get_albums_for_user(username)
    except pylast.WSError:
        flash(u"Sorry, the user '%s' does not exist on LastFM" % username, "error")
        return redirect(url_for('get_user'))

    return render_template('albums.html', albums=albums, username=username)

if __name__ == '__main__':
    app.debug = True
    app.secret_key = HEROKU_SECRET
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
