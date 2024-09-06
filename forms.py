from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, AnyOf, URL, NumberRange, Optional

class AddPetForm(FlaskForm):

    pet_name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'], message="Species must be either cat, dog, or porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Invalid URL format")])
    age = FloatField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Invalid URL format")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available", validators=[Optional()])
    