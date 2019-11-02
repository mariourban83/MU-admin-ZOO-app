from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

# Create Flask Form for Adding New Animal to DB
class AnimalForm(FlaskForm):
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