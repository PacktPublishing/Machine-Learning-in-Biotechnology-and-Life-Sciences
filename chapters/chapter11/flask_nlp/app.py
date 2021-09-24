from flask import Flask, jsonify, request, render_template 
import json
from transformers import pipeline
import re

app = Flask(__name__, template_folder='templates')

summarizer = pipeline("summarization")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction', methods = ["POST"])
def prediction():
    """
    A function that takes a JSON with two fields: "text" and "maxlen"
    Returns: the summarized text of the paragraphs.
    """
    print(request.form.values())
    paragraphs = request.form.get("paragraphs")
    paragraphs = re.sub("\d+", "", paragraphs)
    maxlen = int(request.form.get("maxlen"))
    summary = summarizer(paragraphs, max_length=maxlen, min_length=49, do_sample=False)
    return render_template('index.html', prediction_text = '" {} "'.format(summary[0]["summary_text"])), 200

@app.route('/api/prediction', methods = ["POST"])
def api_prediction():
    """
    A function that takes a JSON with two fields: "text" and "maxlen"
    Returns: the summarized text of the paragraphs.
    """
    query = json.loads(request.data)
    paragraphs = re.sub("\d+", "", query["text"])
    maxlen = query["maxlen"]
    minlen = query["minlen"]
    summary = summarizer(paragraphs, max_length=maxlen, min_length=minlen, do_sample=False)
    return jsonify(summary), 200

if __name__ == '__main__':
    app.run(debug=True)