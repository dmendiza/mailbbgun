import flask

app = flask.Flask(__name__)
app.config.from_object('config')

from mailbbgun import views  # noqa: E402,F401
