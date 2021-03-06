import os
import flask
from position import get_position

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html', position = get_position())

@app.route('/api')
def api():
    return get_position()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)