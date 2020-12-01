from flask import Flask, redirect, render_template, Blueprint
from app import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<name>') 
def greet(name): 
    return f"Hello {name}!"