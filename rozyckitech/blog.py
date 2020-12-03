import functools

from flask import Blueprint, render_template

bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.route('/')
def main():
    return render_template('blog/index.html')