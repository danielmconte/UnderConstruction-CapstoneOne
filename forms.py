from flask_wtf import FlaskForm
from wtforms import IntegerField,  SelectField, BooleanField
from wtforms.validators import InputRequired

# Class forms below (as needed)
class AddPhotoForm(FlaskForm):

    rover = SelectField("Rover", choices=[('curiosity', 'Curiosity'), ('spirit','Spirit'), ('insight', 'Insight'), ('perseverance', 'Perseverance')], validators=[InputRequired()])
    sol= IntegerField("Sol", validators=[InputRequired()])
    album = BooleanField("Save to Album")