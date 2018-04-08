from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

##################
### Functions  ###
##################
def initializeDB(app):
	config = json.load(open('config.json'))
	if config["deployment"] == "local":
		app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////tmp/murals.db' 
	elif config["deployment"] == "server":
		SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
			username="Quack4ACause",
			password="noSleep69",
			hostname="Quack4ACause.mysql.pythonanywhere-services.com",
			databasename="Quack4ACause$murals",
		)
		app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
	
	app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
	db.app = app
	db.init_app(app)

	db.drop_all() # Clear all prior entries
	populateDB() # Repopulate DB with fresh entries
	db.session.commit()

def populateDB():
	db.create_all()
	dbJsonData = json.load(open('murals.json'))
	for mural in dbJsonData["murals"]:
		newMural = Mural(
			# Internal info
			photoPathName = mural["name"].replace(" ", ""),

			# Content info
			muralName = mural["muralName"],
			artistName = mural["name"],
			country = mural["country"],
			description = mural["description"],
			locationDesc = mural["locationDesc"],
			artistDesc = mural["artistDesc"],
			website = mural["website"],
			youtube = mural["youtube"],
			dateInTown = mural["dateInTown"],
			instagramHtml = mural["html"],
			hasYoutube = (mural["youtube"] != ""),
			hasBeforeShot = mural["hasBeforeShot"],

			# Google Map info
			latitude = mural["lat"],
			longitude = mural["long"],
			pitch = mural["pitch"],
			heading = mural["heading"],
			zoom = mural["zoom"]
		)

		db.session.add(newMural)

###############
### Models  ###
###############
class Mural(db.Model):

	# Internal info
	__tablename__ = "murals"
	id = db.Column(db.Integer, primary_key = True) # Unique ID
	photoPathName = db.Column(db.String(32)) # Name of path to photo folder

	# Content info
	muralName = db.Column(db.String(64)) # Name of the mural
	artistName = db.Column(db.String(64)) # artist or business name
	country = db.Column(db.String(64)) # Name of country of origin
	description = db.Column(db.String(4096)) # description of the mural
	instagramHtml = db.Column(db.String(4096)) # html as string for insta embed
	artistDesc = db.Column(db.String(4096)) # About the artist/company
	locationDesc = db.Column(db.String(128)) # Where the mural is
	dateInTown = db.Column(db.String(64)) # When the artist made the mural
	website = db.Column(db.String(128)) # url of the artists webpage
	youtube = db.Column(db.String(128)) # url of the youtube video
	hasYoutube = db.Column(db.Boolean) # Has a youtube video
	hasBeforeShot = db.Column(db.Boolean) # Has a before (and after) shot of the mural

	# Google Map info
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	pitch = db.Column(db.Float)
	heading = db.Column(db.Float)
	zoom = db.Column(db.Float)


	def printOut(self):
		print str(self.id) + "). mural: " + self.muralName + ", artist: " + self.artistName + ", country: " + self.country + ", path: " + self.photoPathName











