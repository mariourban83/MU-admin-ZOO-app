from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email,EqualTo

# Create Flask Login Form 
class LoginForm(FlaskForm):
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')                    
    submit = SubmitField('Login')

# Create Flask Registration Form 
class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])                        
    submit = SubmitField('Sign Up')

# Create Flask Form for Adding New Animal to DB
class AnimalForm(FlaskForm):
    common_name = StringField('Common name :', validators=[DataRequired()])
    scientific_name = StringField('Scientific name :', validators=[DataRequired()])
    diet = StringField('Diet :', validators=[DataRequired()])
    avg_lifespan = StringField('Avg lifespan :', validators=[DataRequired()])
    size = StringField('Size :', validators=[DataRequired()])
    weight = StringField('Weight :', validators=[DataRequired()])
    about = TextAreaField('About (optional) :')
    behavior = TextAreaField('Behavior (optional) :')
    facts = TextAreaField('Facts (optional):')
    img = StringField('Link to Image :', validators=[DataRequired()])
    source = StringField('Source :', validators=[DataRequired()])
    section = StringField('Section :', validators=[DataRequired()])
    other = TextAreaField('Other (optional) :')
    submit = SubmitField('Submit')