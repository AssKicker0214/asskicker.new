from flask import Flask, render_template, request, url_for, jsonify, Response, redirect
import logics.authentication as aut
import json

app = Flask(__name__)


def require_login(original_function):
    """
    Interrupt the original function, check whether user has logged in,
    if not, redirect to login page;
    else, continue with the original_function
    :param original_function: the function that would be interrupted
    :return:
    """

    def wrapper(*args, **kwargs):
        token = request.cookies.get("token")
        # return login(goto=request.full_path) if token is None or not aut.check_login(token) \
        #     else original_function(*args, **kwargs)
        return redirect('/login?goto=%s' % request.full_path) \
            if token is None or not aut.check_login(token) \
            else original_function(*args, **kwargs)

    return wrapper


@app.route('/login')
def login(goto='/welcome'):
    """
    Forward a login page. This login action act as an interruption before accessing
    some sensitive information. The original action will be automatically performed
    if the login is a success.
    :param goto: the target URL to go, after successfully log into the system
    :return: login page
    """
    args = request.args
    real_goto = args['goto'] if 'goto' in args else goto
    return render_template('login.html', goto=real_goto)


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
@app.route('/new-article')
@require_login
def edit_article(article_name: str = None):
    """

    :param article_name: creating if `article_name` is an empty string,
                        else return an existing article or 404 error.
    :return:
    """
    return render_template('edit-article.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3333, debug=True)
