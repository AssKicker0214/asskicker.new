import json
import re

from flask import Flask, render_template, request, jsonify, Response, redirect

import logics.authentication as aut
import logics.uploader as uploader
import utils.config as conf
from logics.article import Article

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
        if not conf.security():
            return original_function(*args, **kwargs)

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
    return render_template('welcome.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/article/<int:article_id>')
def article_page(article_id: int):
    article = Article(aid=article_id)
    return render_template('read-article.html', **article.get_meta()) \
        if article.exists else 404


@app.route('/editor/<int:article_id>')
@app.route('/editor/new')
@require_login
def edit_article(article_id: int = None):
    """

    :param article_id: create if `article_id` is None,
                        else return an existing article or 404 error.
    :return:
    """
    article = Article(aid=article_id)
    return redirect('/editor/new') \
        if not article.exists and article_id is not None \
        else render_template('edit-article.html', **article.get_meta())


@app.route('/get-article')
def get_article():
    args = request.args
    aid = int(args['aid']) \
        if 'aid' in args and re.compile(r'\d+').match(args['aid']) \
        else None
    article = Article(aid=aid)
    return Response(json.dumps(article.get(), ensure_ascii=False, indent=2),
                    mimetype='application/json')


@app.route('/update-article', methods=['POST'])
def update_article():
    body = request.json
    data = body['data']
    article = Article(aid=data['_id'])
    aid = article.update(data, and_save=True)
    return jsonify(result=True, aid=aid)


@app.route('/upload-article-img', methods=['POST'])
def upload_article_img():
    files = request.files.items()
    urls = []
    for _, file in files:
        urls.append(uploader.upload_img(file))
    return jsonify(result=True, urls=urls)


@app.route('/article-list')
def article_list_page():
    return render_template('article-list.html')


@app.route('/list-article')
def list_article():
    token = request.cookies.get('token')
    show_private = aut.check_login(token)
    articles = Article.get_all(public_only=not show_private)
    metas = list(map(lambda a: a.get_meta(), articles))
    return jsonify(metas)


# todo The order of `require_login` and `app.route` cannot change, why?
@require_login
@app.route('/topic-config')
def topic_config_page():
    return render_template('topic_config.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=conf.expose_port(), debug=True)
