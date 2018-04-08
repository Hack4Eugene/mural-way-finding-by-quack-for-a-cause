#####################
### Dependencies  ###
#####################
from flask import Flask, request, render_template, redirect
from models import db, Mural, initializeDB
import os

################
### Globals  ###
################
app = Flask(__name__)
initializeDB(app)
murals = Mural.query.all()

DEBUG = False

if (DEBUG):
	print "Mural count: " + str(len(murals))
	for mural in murals:
		mural.printOut()

###############
### Routes  ###
###############
@app.route('/')
def mainPage():
	# muralData is a 2D array with the following values in each element:
	# [id, latitude, longitude]
	muralData = Mural.query.with_entities(Mural.id, Mural.latitude, Mural.longitude, Mural.artistName, Mural.locationDesc, Mural.photoPathName).all()
	return render_template('index.html', murals=muralData)

@app.route('/mural/')
@app.route('/mural/<muralID>')
def hello(muralID=0):
	mural = Mural.query.get(int(muralID))

	if (mural == None):
		return redirect('/')

	if (mural.youtube != ""):
		print mural.youtube

	return render_template('mural.html', Mural=mural)


@app.route('/test')
def test():
	mural = Mural.query.get(2)
	return render_template('oembedTest.html', Mural=mural)
