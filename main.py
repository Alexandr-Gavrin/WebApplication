import os
from flask import Flask

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
def index():
    return 'Привет приложение фласк'


if __name__ == '__main__':
    port = int(os.environ.get('port', 5000))
    app.run(host='0.0.0.0', port=port)
