from flask import Flask, jsonify, request, render_template 
import json
from transformers import pipeline
import re

app = Flask(__name__, template_folder='templates')

summarizer = pipeline("summarization")

@app.route('/')
def biotech():
    return "Hello Biotech World!"

@app.route('/lifescience')
def lifescience():
    return "Hello Life Science World!"

if __name__ == '__main__':
    app.run(debug=True)