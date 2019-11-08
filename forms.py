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
    username = StringField('*Username (5 - 20 characters)', 
                            validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('*Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('*Password (5 - 10 characters)', validators=[DataRequired(), Length(min=5, max=10)])
    confirm_password = PasswordField('*Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])                        
    submit = SubmitField('Sign Up')

# Flask Form for Adding or updating Animals to the mongoDB
class AnimalForm(FlaskForm):
    common_name = StringField('*Animal Name :', validators=[DataRequired()])
    scientific_name = StringField('Scientific name :')
    diet = StringField('Diet :')
    avg_lifespan = StringField('Avg lifespan :')
    size = StringField('Size :')
    weight = StringField('Weight :')
    about = TextAreaField('About :')
    behavior = TextAreaField('Behavior :')
    facts = TextAreaField('Facts :')
    img = StringField('*Image url:', validators=[DataRequired()])
    source = StringField('Source of info entered :')
    other = TextAreaField('Other :')
    submit = SubmitField('Submit')
