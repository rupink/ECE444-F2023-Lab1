from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    uoft = EmailField('What is your UofT Email Address?', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])

def index():
    name = None
    uoft = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_uoft = session.get('uoft')
        #name = form.name.data
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_uoft is not None and old_uoft != form.uoft.data:
            flash('Looks like you have changed your Email!')
        session['name'] = form.name.data
        session['uoft'] = form.uoft.data
        return redirect(url_for('index'))
    return render_template('index.html',
        form = form, name = session.get('name'), uoft = session.get('uoft'))
'''
        #uoft = form.uoft.data
        form.name.data = ''
        #form.uoft.data = ''
    #return render_template('index.html', form=form, name=name)#, uoft = uoft)'''

@app.route('/user/<name>')
def user(name):
    return ('<h1> Hello , {}! </h1>'.format(name))
