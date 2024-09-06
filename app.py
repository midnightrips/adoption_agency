from flask import Flask, render_template, redirect, request, session, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = '12345'
app.config['DEBUG_TB_INTEREPT_REDIRECTS'] = False
app.debug = True
debug = DebugToolbarExtension(app)

app_context = app.app_context()
app_context.push()
connect_db(app)
db.drop_all()
db.create_all()

@app.route('/')
def list_pets():
    """List of pets."""
    pets =  Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def show_add_pet_form():
    """Show form for adding a pet."""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        
        db.session.add(pet)
        db.session.commit()
        
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet(pet_id):
    """Show pet details page."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.availble = form.available.data
        db.session.commit()  # Save changes to the database
        return redirect(f"/{pet_id}")
    else:
        return render_template('pet_details.html', pet=pet, form=form)