from flask import Blueprint, render_template
from controllers import create_post, edit_post, delete_post, get_post, check_authenticated, authenticate, show_post

blueprint = Blueprint('main', __name__)

@blueprint.route('/')
def index():
    posts = get_post()
    return render_template('index.html', posts=posts)

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return authenticate()

@blueprint.route('/admin')
def admin():
    return check_authenticated()

@blueprint.route('/admin/create', methods=['GET', 'POST'])
def create():
    return create_post()

@blueprint.route('/admin/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    return edit_post(post_id)

@blueprint.route('/admin/delete/<int:post_id>', methods=['GET', 'POST'])
def delete(post_id):
    return delete_post(post_id)

@blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_message='Página não encontrada'), 404

@blueprint.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    return show_post(post_id)
