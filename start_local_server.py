"""
==============================
@author: bmz
@contact: bomz@dianzhong.com
@software: PyCharm
@file: start_local_server.py
@time: 2020/9/16 19:16
@desc:
==============================
"""
import flask

from flask import jsonify
app = flask.Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return jsonify({"code": 1, "msg": "hello python"})


if __name__ == '__main__':
    app.run(debug=True)