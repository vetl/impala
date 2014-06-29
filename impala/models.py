from flask import redirect, session, url_for
from functools import wraps
from mpd import MPDClient, MPDError

client = MPDClient()

def require_mpd(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            client.ping()
        except (MPDError, OSError):
            return redirect(url_for('connect'))
        return func(*args, **kwargs)
    return wrapper
