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
        DATABASE=os.path.join(app.instance_path, 'simple-api.sqlite'),
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

    @app.route("/")
    def index():
        return "<p>Hello, World!</p>"

    @app.route('/dashboard')
    def dashboard():
        if 'logged_in' in session:
            return "Welcome to your dashboard!"
        return redirect(url_for('login', next=request.endpoint))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['username'] = request.form['username']
            session["logged_in"] = True
            # Redirect to the next page or the dashboard
            next_page = request.args.get('next', 'dashboard')
            return redirect(url_for(next_page))
        return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''

    @app.route('/logout')
    def logout():
        # remove the username from the session if it's there
        session.pop('username', None)
        return redirect(url_for('index'))

    from . import db
    db.init_app(app)

    return app


# TODO: Blueprints and Views: https://flask.palletsprojects.com/en/3.0.x/tutorial/views/
