import os

from flask import (
    Flask,
    redirect,
    request,
    session,
    url_for,
)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'simple_api.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/dashboard')
    def dashboard():
        if 'logged_in' in session:
            return "Welcome to your dashboard!"
        return redirect(url_for('login', next=request.endpoint))

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import item
    app.register_blueprint(item.bp)
    app.add_url_rule('/', endpoint='index')

    return app


# TODO: Blog Blueprint https://flask.palletsprojects.com/en/3.0.x/tutorial/blog/
