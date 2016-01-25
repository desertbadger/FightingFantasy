from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired



class HeroStats(Form):
    hstam = StringField('hstam', validators=[DataRequired()])
    hskill = StringField('hskill', validators=[DataRequired()])
    hluck = StringField('hluck', validators=[DataRequired()])
    estam = StringField('estam', validators=[DataRequired()])
    eskill = StringField('eskill', validators=[DataRequired()])


class LoginForm(Form):
    username = StringField('Your Username:', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
