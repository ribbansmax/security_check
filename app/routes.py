from app import app
from flask import Flask, Blueprint, request, jsonify, render_template, redirect, url_for, flash

@app.route('/')
def index():
    
    return render_template('index.html')
