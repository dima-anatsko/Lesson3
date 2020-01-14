from flask import Flask, request, render_template
import json

import calories


app = Flask(__name__)


@app.route('/')
def index():
    if "application/json" in request.environ.get('HTTP_ACCEPT'):
        eats = json.loads(request.data)
        return json.dumps(calories.sum_cal(eats))
    else:
        return render_template('eat.html')


if __name__ == '__main__':
    app.run()
