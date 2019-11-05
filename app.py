# Modules and libraries imported
import os
from flask import Flask, render_template, url_for,flash, redirect, request
from flask_pymongo import PyMongo
from forms import AnimalForm, LoginForm, RegistrationForm
from bson.objectid import ObjectId

# Config files for the app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bd57fa89f3141ef0b5546c8967a93507'
app.config["MONGO_URI"] = 'mongodb+srv://mario_1:PEgPBNn89YWJ4GYQ@testing1-kwpyu.mongodb.net/zoo?retryWrites=true&w=majority'
mongo = PyMongo(app)

# Route for Home view
@app.route("/")
@app.route('/home')
def home(): 
    return render_template('index.html',title='Home')

#  Route for Animals view with all animals pulled from mongoDB and displayed
@app.route('/animals')
def animals():
    animals = mongo.db.animals.find() 
    return render_template('animals.html',title='Animals', animals=animals) 

#  Route for new animal view- for adding new animal to the mongoDB   
@app.route('/new',methods=['GET','POST'])
def new_animal():
    form = AnimalForm()
    if request.method == 'POST':
            mongo.db.animals.insert_one(form.data)
            flash(f'New Animal Added for {form.common_name.data}!', 'success')
            return redirect(url_for('animals'))
    return render_template('new_animal.html',title='Add new Animal', form=form )


#  Route for editing existing animal
#  After selecting edit-animal on page, data are transfered and populated 
#  in the form ready for editing
@app.route('/edit_animal/<animal_id>')
def edit_animal(animal_id):
    animal =  mongo.db.animals.find_one({"_id": ObjectId(animal_id)})
    return render_template('edit_animal.html', animal=animal,title='Edit Animal')

# Function called after submitting for updating animal in mongoDB
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
    return redirect(url_for('animals'))

#  Route for removing animal from the database
@app.route('/delete_animal/<animal_id>')
def delete_animal(animal_id):
    mongo.db.animals.remove({'_id': ObjectId(animal_id)})
    return redirect(url_for('animals'))

#  Default route , sets Login as landing view page
#  Form from forms.py used for both login and register page
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@zoo.com' and form.password.data == 'password':
            flash(f'Login Successful for {form.email.data}!', 'success')
            return redirect(url_for('home'))
        else:
             flash('Login Unsuccessful! Please check username and password', 'danger')  
    return render_template('login.html',title='Login', form=form )    

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form )

if __name__ == '__main__':
    app.run(debug = True) 