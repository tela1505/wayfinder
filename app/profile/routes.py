from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import current_user
from sqlalchemy.exc import IntegrityError
from app import db
from app.profile.forms import WeightEntryForm, SleepEntryForm, GradeEntryForm
from app.models import Weight, Sleep, Grade, User
from app.profile import bp_prof


@bp_prof.route('/profile', methods=['POST', 'GET'])
def profile():
    weight_form = WeightEntryForm()
    sleep_form = SleepEntryForm()
    grade_form = GradeEntryForm()
    if request.method == 'POST' and weight_form.validate():
        weight = Weight(weight=weight_form.weight.data, date=weight_form.date.data, userId=current_user.userId)
        try:
            print("passed")
            db.session.add(weight)
            db.session.commit()
            flash('You have submitted your weight!')
            return redirect(url_for('prof.profile'))
        except IntegrityError:
            db.session.rollback()
            flash('ERROR! Unable to submit weight of {}. Please check your details are correct and resubmit'.format(
                weight_form.weight.data), 'error')
    if request.method == 'POST' and sleep_form.validate():
        sleep = Sleep(sleep=sleep_form.sleep.data, date=sleep_form.date.data, userId=current_user.userId)
        try:
            print("passed")
            db.session.add(sleep)
            db.session.commit()
            flash('You have submitted your sleep!')
            return redirect(url_for('prof.profile'))
        except IntegrityError:
            db.session.rollback()
            flash('ERROR! Unable to submit weight of {}. Please check your details are correct and resubmit'.format(
                weight_form.weight.data), 'error')
    if request.method == 'POST' and grade_form.validate():
        grade = Grade(grade=grade_form.grade.data, gradeSubject=grade_form.gradeSubject.data, date=grade_form.date.data,
                      userId=current_user.userId)
        try:
            print("passed")
            db.session.add(grade)
            db.session.commit()
            flash('You have submitted your grade!')
            return redirect(url_for('prof.profile'))
        except IntegrityError:
            db.session.rollback()
            flash('ERROR! Unable to submit the grade of {}. Please check your details are correct and resubmit'.format(
                grade_form.grade.data), 'error')

    weightlabels = Weight.query.with_entities(Weight.date).filter_by(userId=current_user.userId).all()
    weightlabels = [str(item).replace("(", "") for item in weightlabels]
    weightlabels = [str(item).replace(")", "") for item in weightlabels]
    weightlabels = [str(item).replace(",", "") for item in weightlabels]
    weightlabels = [str(item).replace("'", "") for item in weightlabels]
    #print(weightlabels)
    weightvalues = Weight.query.with_entities(Weight.weight).filter_by(userId=current_user.userId).all()
    weightvalues = [str(item).replace("(", "") for item in weightvalues]
    weightvalues = [str(item).replace(")", "") for item in weightvalues]
    weightvalues = [str(item).replace(",", "") for item in weightvalues]
    #print(weightvalues)

    sleeplabels = Sleep.query.with_entities(Sleep.date).filter_by(userId=current_user.userId).all()
    sleeplabels = [str(item).replace("(", "") for item in sleeplabels]
    sleeplabels = [str(item).replace(")", "") for item in sleeplabels]
    sleeplabels = [str(item).replace(",", "") for item in sleeplabels]
    sleeplabels = [str(item).replace("'", "") for item in sleeplabels]
    # print(sleeplabels)
    sleepvalues = Weight.query.with_entities(Sleep.sleep).filter_by(userId=current_user.userId).all()
    sleepvalues = [str(item).replace("(", "") for item in sleepvalues]
    sleepvalues = [str(item).replace(")", "") for item in sleepvalues]
    sleepvalues = [str(item).replace(",", "") for item in sleepvalues]
    # print(sleepvalues)

    gradelabels = Grade.query.with_entities(Grade.date).filter_by(userId=current_user.userId).all()
    gradelabels = [str(item).replace("(", "") for item in gradelabels]
    gradelabels = [str(item).replace(")", "") for item in gradelabels]
    gradelabels = [str(item).replace(",", "") for item in gradelabels]
    gradelabels = [str(item).replace("'", "") for item in gradelabels]
    # print(gradelabels)
    gradevalues = Weight.query.with_entities(Grade.grade).filter_by(userId=current_user.userId).all()
    gradevalues = [str(item).replace("(", "") for item in gradevalues]
    gradevalues = [str(item).replace(")", "") for item in gradevalues]
    gradevalues = [str(item).replace(",", "") for item in gradevalues]
    # print(gradevalues)
    gradesubject = Weight.query.with_entities(Grade.gradeSubject).filter_by(userId=current_user.userId).all()
    gradesubject = [str(item).replace("(", "") for item in gradesubject]
    gradesubject = [str(item).replace(")", "") for item in gradesubject]
    gradesubject = [str(item).replace(",", "") for item in gradesubject]
    gradesubject = [str(item).replace("'", "") for item in gradesubject]
    print(gradesubject)

    return render_template('profile.html', weight_form=weight_form, sleep_form=sleep_form, grade_form=grade_form, weightlabels=weightlabels, weightvalues=weightvalues, sleeplabels=sleeplabels, sleepvalues=sleepvalues, gradelabels=gradelabels, gradevalues=gradevalues, gradesubject=gradesubject)
