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



@bp_main.route('/gamedev')
def gamedev():
    return render_template('game_development/gamedev_overview.html')


@bp_main.route('/gamedev/1')
def gamedev1():
    return render_template('game_development/gamedev_step1.html')


@bp_main.route('/gamedev/2')
def gamedev2():
    return render_template('game_development/gamedev_step2.html')


@bp_main.route('/gamedev/3')
def gamedev3():
    return render_template('game_development/gamedev_step3.html')


@bp_main.route('/gamedev/4')
def gamedev4():
    return render_template('game_development/gamedev_step4.html')


@bp_main.route('/gamedev/finish')
def gamedev_finish():
    return render_template('game_development/gamedev_finished.html')



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


@bp_main.route('/webdev/finish')
def webdev_finish():
    return render_template('web_development/webdev_finished.html')



@bp_main.route('/mathematician')
def mathematician():
    return render_template('mathematician/mathematician_overview.html')


@bp_main.route('/mathematician/1')
def mathematician1():
    return render_template('mathematician/mathematician_step1.html')


@bp_main.route('/mathematician/2')
def mathematician2():
    return render_template('mathematician/mathematician_step2.html')


@bp_main.route('/mathematician/3')
def mathematician3():
    return render_template('mathematician/mathematician_step3.html')


@bp_main.route('/mathematician/4')
def mathematician4():
    return render_template('mathematician/mathematician_step4.html')


@bp_main.route('/mathematician/finish')
def mathematician_finish():
    return render_template('mathematician/mathematician_finished.html')



@bp_main.route('/trainer')
def trainer():
    return render_template('personal_trainer/trainer_overview.html')


@bp_main.route('/trainer/1')
def trainer1():
    return render_template('personal_trainer/trainer_step1.html')


@bp_main.route('/trainer/2')
def trainer2():
    return render_template('personal_trainer/trainer_step2.html')


@bp_main.route('/trainer/3')
def trainer3():
    return render_template('personal_trainer/trainer_step3.html')


@bp_main.route('/trainer/4')
def trainer4():
    return render_template('personal_trainer/trainer_step4.html')


@bp_main.route('/trainer/finish')
def trainer_finish():
    return render_template('personal_trainer/trainer_finished.html')



@bp_main.route('/medicine')
def medicine():
    return render_template('medicine/medicine_overview.html')


@bp_main.route('/medicine/1')
def medicine1():
    return render_template('medicine/medicine_step1.html')


@bp_main.route('/medicine/2')
def medicine2():
    return render_template('medicine/medicine_step2.html')


@bp_main.route('/medicine/3')
def medicine3():
    return render_template('medicine/medicine_step3.html')


@bp_main.route('/medicine/4')
def medicine4():
    return render_template('medicine/medicine_step4.html')


@bp_main.route('/medicine/finish')
def medicine_finish():
    return render_template('medicine/medicine_finished.html')