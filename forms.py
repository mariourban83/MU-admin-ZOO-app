from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email,EqualTo

# Create Flask Form for Adding New Animal to DB
class AddAnimalForm(FlaskForm):
    common_name = StringField('Common name :', validators=[DataRequired()])
    scientific_name = StringField('Scientific name :', validators=[DataRequired()])
    diet = TextAreaField('Diet :', validators=[DataRequired()])
    avg_lifespan = TextAreaField('Avg lifespan :', validators=[DataRequired()])
    size = TextAreaField('Size :', validators=[DataRequired()])
    weight = TextAreaField('Weight :', validators=[DataRequired()])
    about = TextAreaField('About :', validators=[DataRequired()])
    behavior = TextAreaField('Behavior :', validators=[DataRequired()])
    facts = TextAreaField('Facts :', validators=[DataRequired()])
    img = TextAreaField('Link to Image :', validators=[DataRequired()])
    source = TextAreaField('Source :', validators=[DataRequired()])
    section = TextAreaField('Section :', validators=[DataRequired()])
    other_optional = TextAreaField('Other-Optional :')

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

