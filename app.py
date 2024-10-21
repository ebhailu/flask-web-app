"""
Ebenezer Hailu
CMSC 426 - Assignment 3 (Flask Web Application)
October 19th, 2024
"""

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

bootstrap = Bootstrap(app)
moment = Moment(app)

class WebForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    studentid = StringField('Student ID', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired()])
    courseNum = StringField('Course Number', validators=[DataRequired()])
    justification = StringField('Justification (Optional)')
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = WebForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['studentid'] = form.studentid.data
        session['course'] = form.course.data
        session['courseNum'] = form.courseNum.data
        session['justification'] = form.justification.data
        flash('Successful submission!')
        
        return redirect(url_for('index'))


    return render_template('index.html', form=form, 
                           name=session.get('name'),
                           studentid=session.get('studentid'),
                           course=session.get('course'),
                           courseNum=session.get('courseNum'),
                           justification=session.get('justification'))

if __name__ == '__main__':
    app.run(debug=True)