# Top Albums

An ultra-simple Flask application to display a user's top 10 albums using the LastFM API

## Requirements

To run this application, a working Python install, with virtualenv is required.

To set this up on Mac OS X, follow [these instructions](http://docs.python-guide.org/en/latest/starting/install/osx/).

## Running Locally

To run the application locally:

- Navigate to the top-albums base directory  
- Install a virtualenv instance: `virtualenv venv`   
- Activate the virtualenv instance: `source venv/bin/activate` 

Now create a file called `app_private.py` and add to it the following lines:

```
LASTFM_API_KEY = "xxxxxxxxx"
LASTFM_SECRET = "xxxxxxxxx"
HEROKU_SECRET = "xxxxxxxxx"
```

Replacing `xxxxxxxxx` with the relevant key.

Then:

- Start the server: `python app.py`
- Navigate to [http://0.0.0.0:5000](http://0.0.0.0:5000)

To terminate the web server and exit the virtualenv:

- ctrl-C
- `deactivate`

## To deploy to Heroku

- It should be sufficient to type: `git push heroku master`





