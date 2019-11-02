import os
from flask import Flask, render_template, url_for,flash, redirect, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb+srv://mario_1:PEgPBNn89YWJ4GYQ@testing1-kwpyu.mongodb.net/zoo?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home(): 
    return render_template('index.html',title='Home')

@app.route('/animals')
def animals():
    animals = mongo.db.animals.find() 
    return render_template('animals.html',title='Animals', animals=animals) 

if __name__ == "__main__":
    app.run(debug=True)    