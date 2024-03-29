import os
import bcrypt
from flask import Flask, render_template, url_for,flash, redirect, request, session
from flask_pymongo import PyMongo
from forms import AnimalForm, LoginForm, RegistrationForm
from bson.objectid import ObjectId


# Config files for the app
app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb+srv://mario_1:PEgPBNn89YWJ4GYQ@testing1-kwpyu.mongodb.net/zoo?retryWrites=true&w=majority'
app.secret_key = os.urandom(24)
mongo = PyMongo(app)

# Route for Default view
@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    # Variable animals set for displaying actual number from db 
    animals=mongo.db.animals.count()
    return render_template('index.html',title='Home',animals=animals)

#----- CRUD OPERATIONS -----

# Create #
# Route for new animal view- for adding new animal to the mongoDB   
@app.route('/new',methods=['GET','POST'])
def new_animal():
    form = AnimalForm()
    if request.method == 'POST':
            mongo.db.animals.insert_one(form.data)
            flash(f'{form.common_name.data} sucessfuly added!', 'success')
            return redirect(url_for('animals'))
            
    return render_template('new_animal.html',title='Add new Animal', form=form )

## READ ##
#  Route for Animals view with all animals pulled from mongoDB displayed
@app.route('/animals')
def animals():
    animals = mongo.db.animals.find() 
    return render_template('animals.html',title='Animals', animals=animals) 

# Route for viewing a single animal page
@app.route('/animal/<animal_id>')
def animal(animal_id):
	animal= mongo.db.animals.find_one({'_id': ObjectId(animal_id)})
	return render_template('animal.html', animal=animal, title=animal['common_name'])

## UPDATE ##
#  Route for editing existing animal
#  After selecting edit-animal, id-based data are transfered from mongo and populated in the form ready for editing
@app.route('/edit_animal/<animal_id>')
def edit_animal(animal_id):
    animal =  mongo.db.animals.find_one({"_id": ObjectId(animal_id)})
    return render_template('edit_animal.html', animal=animal,title='Edit Animal')

# Function called after submitting form for updating animal in mongoDB
@app.route('/update_animal/<animal_id>', methods=['GET','POST'])
def update_animal(animal_id):
    animals = mongo.db.animals
    animals.update( {'_id': ObjectId(animal_id)},
    {
        'common_name':request.form.get('common_name'),
        'scientific_name':request.form.get('scientific_name'),
        'diet': request.form.get('diet'),
        'avg_lifespan': request.form.get('avg_lifespan'),
        'size':request.form.get('size'),
        'weight':request.form.get('weight'),
        'about':request.form.get('about'),
        'behavior':request.form.get('behavior'),
        'facts':request.form.get('facts'),
        'img':request.form.get('img'),
        'source':request.form.get('source'),
        'section':request.form.get('section')
    })
    flash(f'Successfuly Updated!', 'success')
    return redirect(url_for('animals'))

## REMOVE ##
#  Route for removing animal from the database
@app.route('/delete_animal/<animal_id>')
def delete_animal(animal_id):
    mongo.db.animals.remove({'_id': ObjectId(animal_id)})
    flash(f'Successfuly Removed!', 'danger')
    return redirect(url_for('animals'))

#  Form from forms.py used for both login and register page
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        user = mongo.db.users.find_one({'username': request.form['username']})
    
        if user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), user['password']) == user['password']:
                session['username'] = request.form['username']
                flash(f'Login Successful for {form.username.data}!', 'success')
                return redirect(url_for('home'))
            else: flash('Password and username doesnt match our records!', 'danger')     
        else: flash('Login Unsuccessful! Please check username or password', 'danger')  
    return render_template('login.html',title='Login', form=form )    

# For registering new users
# Use of bcrypt for hashing passwords (hashed password stored in db)
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    users = mongo.db.users
    if form.validate_on_submit() and request.method == 'POST':
        existing_user = users.find_one({'email' : request.form['email']})
        
        if existing_user is None:
                hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
                users.insert({'username' : request.form['username'],'email' : request.form['email'], 'password' : hashpass})
                session['email'] = request.form['email']
                flash(f'Account Created for {form.username.data}!', 'success')
                return redirect(url_for('home'))
        flash('Unsuccessful! Username or email already in use!', 'danger')
    return render_template('register.html', title='Register', form=form)

# Account page with user info tbc.....
@app.route('/account')
def account():
    return render_template('account.html',title='Your Account')            

if __name__ == '__main__':
	app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=False)  