from flask import render_template, Blueprint

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def home():
    return render_template('index.html')


@bp_main.route('/emailing')
def cold():
    return render_template('resources/cold.html')


@bp_main.route('/cv')
def cv():
    return render_template('resources/cv.html')



@bp_main.route('/fashion')
def fashion():
    return render_template('fashion_management/fashion_overview.html')


@bp_main.route('/fashion/1')
def fashion1():
    return render_template('fashion_management/fashion_step1.html')


@bp_main.route('/fashion/2')
def fashion2():
    return render_template('fashion_management/fashion_step2.html')


@bp_main.route('/fashion/3')
def fashion3():
    return render_template('fashion_management/fashion_step3.html')


@bp_main.route('/fashion/4')
def fashion4():
    return render_template('fashion_management/fashion_step4.html')


@bp_main.route('/fashion/finish')
def fashion_finish():
    return render_template('fashion_management/fashion_finished.html')




@bp_main.route('/webdev')
def webdev():
    return render_template('web_development/webdev_overview.html')


@bp_main.route('/webdev/1')
def webdev1():
    return render_template('web_development/webdev_step1.html')


@bp_main.route('/webdev/2')
def webdev2():
    return render_template('web_development/webdev_step2.html')


@bp_main.route('/webdev/3')
def webdev3():
    return render_template('web_development/webdev_step3.html')


@bp_main.route('/webdev/4')
def webdev4():
    return render_template('web_development/webdev_step4.html')
