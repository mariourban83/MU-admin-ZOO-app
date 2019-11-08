from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email,EqualTo

# Flask Login Form 
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])                   
    submit = SubmitField('Login')

# Flask Registration Form 
class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=10)])
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])                        
    submit = SubmitField('Sign Up')

# Flask Form for Adding or updating Animals to the mongoDB
class AnimalForm(FlaskForm):
    common_name = StringField('Common name :', validators=[DataRequired()])
    scientific_name = StringField('Scientific name :')
    diet = StringField('Diet :')
    avg_lifespan = StringField('Avg lifespan :')
    size = StringField('Size :')
    weight = StringField('Weight :')
    about = TextAreaField('About (optional) :')
    behavior = TextAreaField('Behavior (optional) :')
    facts = TextAreaField('Facts (optional):')
    img = StringField('Image url:', validators=[DataRequired()])
    source = StringField('Source of info entered:')
    section = StringField('Section :')
    other = TextAreaField('Other (optional) :')
    submit = SubmitField('Submit')
