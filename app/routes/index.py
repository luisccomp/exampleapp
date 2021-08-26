from flask import Blueprint, render_template

from app.services import posts_service

blueprint = Blueprint('index', __name__)


def register_blueprint(app):
    app.register_blueprint(blueprint)


@blueprint.route('/')
@blueprint.route('/index')
def index():
    # Instead of doing all queries inside of view function, I prefer to do this
    # instead of almost all of flask tutorials I find on internet.
    posts = posts_service.find_all_posts()

    return render_template('index.html', title='Microblog', posts=posts)
