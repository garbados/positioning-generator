import flask
from position import get_position

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html', position = get_position())

if __name__ == '__main__':
    app.run(debug=True)