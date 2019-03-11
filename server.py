import os
import test
import Project_Lyrics_Generator
from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import jsonify
app = Flask(__name__)

@app.route('/result')
def result():
	return Project_Lyrics_Generator.LyricsGenerator()
	




@app.route('/', methods = ['GET', 'POST'])
def hello():
	return  render_template("getInput.html")








if __name__ == '__main__':
    app.run(debug=True)