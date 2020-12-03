import functools

from flask import Blueprint, render_template

bp = Blueprint('about', __name__, url_prefix='/about')

@bp.route('/me')
def me():
    return render_template('about/index.html')

@bp.route('/trainings')
def trainings():
    return render_template('about/trainings.html')

@bp.route('/software_development')
def software():
    return render_template('about/software_development.html')

@bp.route('/contact')
def contact():
    return render_template('about/contact.html')