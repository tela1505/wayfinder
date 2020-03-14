from flask import render_template, Blueprint

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def home():
    return render_template('index.html')


@bp_main.route('/fashion')
def fashion():
    return render_template('fashion_management/fashion_overview.html')
