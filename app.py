import os
from flask import Flask, render_template, url_for,flash, redirect, request
from flask_pymongo import PyMongo
from forms import AnimalForm, LoginForm, RegistrationForm
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bd57fa89f3141ef0b5546c8967a93507'
app.config["MONGO_URI"] = 'mongodb+srv://mario_1:PEgPBNn89YWJ4GYQ@testing1-kwpyu.mongodb.net/zoo?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/home')
def home(): 
    return render_template('index.html',title='Home')

@app.route('/animals')
def animals():
    animals = mongo.db.animals.find() 
    return render_template('animals.html',title='Animals', animals=animals) 

@app.route('/animals/new',methods=['GET','POST'])
def new_animal():
    form = AnimalForm()
    if form.validate_on_submit():
        if form.data:
            mongo.db.animals.insert_one(request.form.to_dict())
            return redirect(url_for('animals'))
        else:
            return redirect(url_for('new_animal'))    
    return render_template('new_animal.html',title='Add New Animal', form=form )

@app.route("/",methods=['GET','POST'])
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

if __name__ == "__main__":
    app.run(debug=True)    