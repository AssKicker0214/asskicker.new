from flask import Flask, render_template, request, url_for, jsonify, Response
import logics.authentication as aut
import json

app = Flask(__name__)


def require_login(func):
    def decorator(*args, **kwargs):
        token = request.cookies.get("token")

        print("mock login success")

    return decorator


@app.route('/login')
def login():
    args = request.args
    goto = args['goto'] if 'goto' in args else url_for("index")
    return render_template('login.html', goto=goto)


@app.route('/test-login', methods=['POST'])
def login_with_hashed_password():
    args = request.json
    hashed = None if 'hashed' not in args else args['hashed']
    result = aut.login_with_hashed_password(hashed)

    res = Response(json.dumps({
        'result': True if result else False
    }), mimetype='application/json')
    if result:
        res.set_cookie("token", result)

    return res


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/welcome')
def welcome():
    pass


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/edit-article/<article_name>')
def edit_article(article_name: str):
    """

    :param article_name: creating if `article_name` is an empty string,
                        else return an existing article or 404 error.
    :return:
    """


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3333, debug=True)
